from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Insert your data here')


class ManualInputForm(forms.Form):
    ALTITUDE = forms.FloatField(label='Altitude')
    ENGINE_LOAD = forms.FloatField(label='Engine Load')
    BAROMETRIC_PRESSURE = forms.FloatField(label='Barometric Pressure')
    ENGINE_COOLANT_TEMP = forms.FloatField(label='Engine Coolant Temperature')
    AMBIENT_AIR_TEMP = forms.FloatField(label='Ambient Air Temperature')
    ENGINE_RPM = forms.FloatField(label='Engine RPM')
    INTAKE_MANIFOLD_PRESSURE = forms.FloatField(label='Intake Manifold Pressure')
    MAF = forms.FloatField(label='MAF')
    AIR_INTAKE_TEMP = forms.FloatField(label='Air Intake Temperature')
    SPEED = forms.FloatField(label='Speed')
    THROTTLE_POS = forms.FloatField(label='Throttle Position')
    ENGINE_RUNTIME = forms.CharField(label='Engine Runtime (HH:MM:SS)')
    TRUCK_SELECT = forms.ChoiceField(choices=[('truck1', 'Truck 1'), ('truck2', 'Truck 2'), ('truck3', 'Truck 3')], label='Select Truck')