"""
URL configuration for tm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
# from . import views

admin.site.site_header = "Welcome, iTrucking Administrator"
admin.site.site_title = "iTrucking Admin"
admin.site.index_title = "iTrucking Administrator"

urlpatterns = [
    path('DoNotAccessTheAdminPageIfYouAreNotAnAdmin/', admin.site.urls, name= 'admin'),
    # path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include('accounts.urls')),
    path('',include('pages.urls')),
    path('',include('booking.urls')),
    path('',include('faces.urls')),
    path('',include('payment.urls')),
    path('',include('maintenance.urls')),
    path('',include('gps.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)