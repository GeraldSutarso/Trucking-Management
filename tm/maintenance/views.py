from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .forms import ExcelUploadForm, ManualInputForm
from .models import ExcelData, UploadedFile, ColumnAverages
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from datetime import datetime
from django.conf import settings
import os
from django.http import FileResponse
from django.conf import settings
from accounts.models import User, Driver, Customer
from django.contrib.auth.decorators import login_required, user_passes_test

def im_customer(user):
    return user.is_customer
def im_superman(user):
    return user.is_superuser
def im_driver(user):
    return user.is_driver

def load_data(file_path):
    df = pd.read_excel(file_path)
    print("Shape of DataFrame before preprocessing:", df.shape)
    print("Columns before preprocessing:", df.columns)
    return df

def preprocess_data(df):
    columns_to_keep = ['ALTITUDE', 'ENGINE_LOAD', 'BAROMETRIC_PRESSURE',
                       'ENGINE_COOLANT_TEMP', 'AMBIENT_AIR_TEMP', 'ENGINE_RPM',
                       'INTAKE_MANIFOLD_PRESSURE', 'MAF', 'AIR_INTAKE_TEMP', 'SPEED', 'THROTTLE_POS', 'ENGINE_RUNTIME']
    df_preprocessed = df[columns_to_keep].copy()
    df_preprocessed['ENGINE_RUNTIME'] = df_preprocessed['ENGINE_RUNTIME'].fillna('00:00:00')
    df_preprocessed['ENGINE_RUNTIME'] = df_preprocessed['ENGINE_RUNTIME'].apply(lambda x: datetime.strptime(str(x), "%H:%M:%S"))
    print(df['ENGINE_RUNTIME'])
    df_preprocessed['ENGINE_RUNTIME'] = df_preprocessed['ENGINE_RUNTIME'].dt.hour * 3600 + df_preprocessed['ENGINE_RUNTIME'].dt.minute * 60 + df_preprocessed['ENGINE_RUNTIME'].dt.second
    print("After rmoving seconds", df['ENGINE_RUNTIME'])
    for column in columns_to_keep:
        df_preprocessed[column] = df_preprocessed[column].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)
        
    
    numerical_columns_updated = df_preprocessed.select_dtypes(include=np.number).columns.tolist()
    
    return df_preprocessed, numerical_columns_updated  

def handle_missing_values(df, numerical_columns):
    imputer = SimpleImputer(strategy='mean')
    imputed_values = imputer.fit_transform(df[numerical_columns])
    df_imputed = pd.DataFrame(imputed_values, columns=numerical_columns)
    return df_imputed

def train_isolation_forest(df, numerical_columns):
    isolation_forest = IsolationForest(contamination="auto", random_state=42)
    outliers = isolation_forest.fit_predict(df[numerical_columns])
    return isolation_forest, outliers

def detect_outliers(isolation_forest, df, numerical_columns):
    outliers = isolation_forest.predict(df[numerical_columns])
    return outliers

def compare_outliers(input_data, outliers):
    outlier_indices = np.where(outliers == -1)[0]
    outlier_rows = input_data.iloc[outlier_indices]
    return outlier_rows

def print_column_averages(df):
    numeric_columns = df.select_dtypes(include=np.number).columns
    numeric_df = df[numeric_columns]
    print("Average value of each numeric column:")
    print(numeric_df.mean())

def sum_anomaly_scores(isolation_forest, df, numerical_columns):
    anomaly_scores = isolation_forest.decision_function(df[numerical_columns])
    total_anomaly_score = np.sum(anomaly_scores)
    return total_anomaly_score

def print_anomaly_scores(isolation_forest, df, numerical_columns):
    anomaly_scores = isolation_forest.decision_function(df[numerical_columns])
    print("Anomaly scores for each input value:")
    for score in anomaly_scores:
        print(score)


@login_required(login_url='login')
@user_passes_test(im_driver, login_url='/login')
def upload_display_excel(request):
    data_to_display = None
    error_message = None
    column_averages = None
    maintenance_status = None
    truck_select = 'truck1'  # Default selection

    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        truck_select = request.POST.get('TRUCK_SELECT', 'truck1')
        print(truck_select)
        if form.is_valid():
            try:
                excel_file = request.FILES['excel_file']
                new_upload = UploadedFile(file=excel_file)
                new_upload.save()

                if truck_select == 'truck2':
                    train_file_path = os.path.join(settings.MEDIA_ROOT, 'training_data', 'badData.xlsx')
                else:
                    train_file_path = os.path.join(settings.MEDIA_ROOT, 'training_data', 'exp2_19drivers_1car_1route.xlsx')
                train_df = load_data(train_file_path)
                train_preprocessed, numerical_columns_updated = preprocess_data(train_df)
                train_imputed = handle_missing_values(train_preprocessed, numerical_columns_updated)

                isolation_forest, _ = train_isolation_forest(train_imputed, numerical_columns_updated)

                file_path = new_upload.file.path
                df = load_data(file_path)
                df_preprocessed, numerical_columns_updated = preprocess_data(df)
                df_imputed = handle_missing_values(df_preprocessed, numerical_columns_updated)

                total_anomaly_score = sum_anomaly_scores(isolation_forest, df_imputed, numerical_columns_updated)
                input_outliers = detect_outliers(isolation_forest, df_imputed, numerical_columns_updated)
                outlier_rows = compare_outliers(df, input_outliers)

                # Calculate column averages
                column_averages = df_imputed.mean().to_dict()

                non_outlier_rows = df.shape[0] - len(outlier_rows)
                outlier_percentage = len(outlier_rows) / len(df) * 100
                print(total_anomaly_score)
                if total_anomaly_score <= -2:
                    maintenance_status = "The vehicle desperately needs maintenance. Status: Severe"
                elif total_anomaly_score <= 0:
                    maintenance_status = "The vehicle needs maintenance. Status: Moderate"
                else:
                    maintenance_status = "Vehicle condition is good."

                # Save to the database
                ColumnAverages.objects.create(
                    altitude_avg=column_averages.get('ALTITUDE', 0),
                    engine_load_avg=column_averages.get('ENGINE_LOAD', 0),
                    barometric_pressure_avg=column_averages.get('BAROMETRIC_PRESSURE', 0),
                    engine_coolant_temp_avg=column_averages.get('ENGINE_COOLANT_TEMP', 0),
                    ambient_air_temp_avg=column_averages.get('AMBIENT_AIR_TEMP', 0),
                    engine_rpm_avg=column_averages.get('ENGINE_RPM', 0),
                    intake_manifold_pressure_avg=column_averages.get('INTAKE_MANIFOLD_PRESSURE', 0),
                    maf_avg=column_averages.get('MAF', 0),
                    air_intake_temp_avg=column_averages.get('AIR_INTAKE_TEMP', 0),
                    speed_avg=column_averages.get('SPEED', 0),
                    throttle_pos_avg=column_averages.get('THROTTLE_POS', 0),
                    engine_runtime_avg=column_averages.get('ENGINE_RUNTIME', 0),
                    maintenance_status=maintenance_status
                )

                # Prepare data to display in HTML format
                data_to_display = outlier_rows.to_html()
                print(data_to_display)
                print(outlier_rows)
            except Exception as e:
                error_message = str(e)
                print(f"Error: {error_message}")
    else:
        form = ExcelUploadForm()

    context = {
        'form': form,
        'data_to_display': data_to_display,
        'error_message': error_message,
        'column_averages': column_averages,
        'maintenance_status': maintenance_status,
        'truck_select': truck_select  # Add this line to pass the selected truck type
    }

    return render(request, 'maintenance/upload_display_excel.html', context)


def determine_maintenance_status(anomaly_score):
    if anomaly_score <= -2:
        return "The vehicle desperately needs maintenance. Status: Severe"
    elif anomaly_score <= 0:
        return "The vehicle needs maintenance. Status: Moderate"
    else:
        return "Vehicle condition is good. Status: Good"

def access_training_data(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'training_data', 'exp2_19drivers_1car_1route.xlsx')

    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        data = df.head().to_dict()
        return JsonResponse({'status': 'success', 'data': data})
    else:
        return JsonResponse({'status': 'error', 'message': 'File not found'})
    

def download_test_case_excel(request):
    # Google Sheets URL
    google_sheets_url = "https://docs.google.com/spreadsheets/d/1fvpAEbKl7ImZaxkihJuoAfEIUVcfxfPR/edit?usp=sharing"

    # Extract file ID from URL
    file_id = google_sheets_url.split("/")[5]

    # Construct direct download link
    direct_download_link = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx"

    # Redirect to direct download link
    return redirect(direct_download_link)




@login_required(login_url='login')
@user_passes_test(im_driver, login_url='/login')
def manual_input_view(request):
    data_to_display = None
    error_message = None
    column_averages = None
    maintenance_status = None

    if request.method == 'POST':
        form = ManualInputForm(request.POST)
        if form.is_valid():
            try:
                truck_select = form.cleaned_data['TRUCK_SELECT']
                print(truck_select)
                # Convert form data to DataFrame
                data = {field: [value] for field, value in form.cleaned_data.items() if field != 'truck_select'}
                print(data)
                df = pd.DataFrame(data)
                print("Columns in the DataFrame:", df.columns)

                # Load and preprocess training data
                if truck_select == 'truck2':
                    train_file_path = os.path.join(settings.MEDIA_ROOT, 'training_data', 'Truck2.xlsx')
                elif truck_select == 'truck3':
                    train_file_path = os.path.join(settings.MEDIA_ROOT, 'training_data', 'Truck3.xlsx')
                else:
                    train_file_path = os.path.join(settings.MEDIA_ROOT, 'training_data', 'exp2_19drivers_1car_1route.xlsx')
                train_df = load_data(train_file_path)
                train_preprocessed, numerical_columns_updated = preprocess_data(train_df)
                train_imputed = handle_missing_values(train_preprocessed, numerical_columns_updated)
                print(train_imputed)
                # Train Isolation Forest model
                isolation_forest, _ = train_isolation_forest(train_imputed, numerical_columns_updated)

                # Preprocess input data
                df_preprocessed, numerical_columns_updated = preprocess_data(df)
                df_imputed = handle_missing_values(df_preprocessed, numerical_columns_updated)
                print(df_imputed)
                # Detect anomalies
                total_anomaly_score = sum_anomaly_scores(isolation_forest, df_imputed, numerical_columns_updated)
                input_outliers = detect_outliers(isolation_forest, df_imputed, numerical_columns_updated)
                outlier_rows = compare_outliers(df, input_outliers)
                print(outlier_rows)
                print(total_anomaly_score)
                # Calculate column averages
                column_averages = df_imputed.mean().to_dict()

                # Determine maintenance status
                maintenance_status = determine_maintenance_status(total_anomaly_score)

                # Save to the database
                ColumnAverages.objects.create(
                    altitude_avg=column_averages.get('ALTITUDE', 0),
                    engine_load_avg=column_averages.get('ENGINE_LOAD', 0),
                    barometric_pressure_avg=column_averages.get('BAROMETRIC_PRESSURE', 0),
                    engine_coolant_temp_avg=column_averages.get('ENGINE_COOLANT_TEMP', 0),
                    ambient_air_temp_avg=column_averages.get('AMBIENT_AIR_TEMP', 0),
                    engine_rpm_avg=column_averages.get('ENGINE_RPM', 0),
                    intake_manifold_pressure_avg=column_averages.get('INTAKE_MANIFOLD_PRESSURE', 0),
                    maf_avg=column_averages.get('MAF', 0),
                    air_intake_temp_avg=column_averages.get('AIR_INTAKE_TEMP', 0),
                    speed_avg=column_averages.get('SPEED', 0),
                    throttle_pos_avg=column_averages.get('THROTTLE_POS', 0),
                    engine_runtime_avg=column_averages.get('ENGINE_RUNTIME', 0),
                    maintenance_status=maintenance_status
                )

                # Prepare data to display in HTML format
                data_to_display = outlier_rows.to_html()
                print(data_to_display)
            except Exception as e:
                error_message = str(e)
                print(f"Error: {error_message}")
    else:
        form = ManualInputForm()

    context = {
        'form': form,
        'data_to_display': data_to_display,
        'error_message': error_message,
        'column_averages': column_averages,
        'maintenance_status': maintenance_status,
    }

    return render(request, 'maintenance/manual_input.html', context)

