from django.urls import path
from . import views
from django.urls import path
from .views import system_info

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('system-info/', system_info, name='system_info'),
]
