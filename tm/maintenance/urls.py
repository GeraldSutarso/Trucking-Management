# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('maintenance/', views.upload_display_excel, name='maintenance_page'),
    path('maintenance2/', views.upload_display_excel),
    path('access-training-data/', views.access_training_data, name='access_training_data'),
    path('download-test-case-excel/', views.download_test_case_excel, name='download_test_case_excel'),
    path('manual-input/', views.manual_input_view, name='manual_input'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)