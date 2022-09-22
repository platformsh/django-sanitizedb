"""bigfoot_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from bigfoot import views

urlpatterns = [
    path('', views.home, name='app_homepage'),
    path('about/', views.about, name='app_about'),
    path('_sightings/', views.sightings_partial, name='app_sightings_partial_list'),
    path('sighting/<int:sighting_id>/', views.sightings_show, name='app_sighting_show'),
    path('admin/', admin.site.urls),
    
]
