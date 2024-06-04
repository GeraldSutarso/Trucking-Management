from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('driver/checkup/', views.checkup_face, name='checkup_face'),
    path('driver/checkup/upload', views.upload_photo_face, name='upload_photo_face'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
