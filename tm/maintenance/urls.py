# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('maintenance/', views.maintenance, name='maintenance_page'),
    path('test/', views.test, name='test'),
    path('import_data_to_db/', views.import_data_to_db),
    path('maintenance2/', views.upload_display_excel),
    path('access-training-data/', views.access_training_data, name='access_training_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)