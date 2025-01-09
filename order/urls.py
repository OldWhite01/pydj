from django.urls import path
from . import views

app_name = 'order'  # 设置命名空间

urlpatterns = [
    path('', views.index, name='index'),
]