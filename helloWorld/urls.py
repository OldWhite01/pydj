from django.urls import path
from . import views

app_name = 'helloWorld'

urlpatterns = [
    path('', views.index, name='index'),
    path('download-page/', views.download_page, name='download_page'),
    path('download/', views.download_file, name='download_file'),
    path('upload/', views.upload_page, name='upload_page'),
    path('upload-file/', views.upload_file, name='upload_file'),
] 