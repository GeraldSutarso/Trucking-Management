# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('maintenance/', views.maintenance, name='maintenance_page'),
    path('test/', views.test, name='test'),
    path('import_data_to_db/', views.import_data_to_db),
    path('maintenance2/', views.upload_display_excel),
]