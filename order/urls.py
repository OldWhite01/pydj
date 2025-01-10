from django.urls import path
from . import views

app_name = 'order'  # 设置命名空间

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.ContentListView.as_view(), name='content_list'),
    path('detail/<int:pk>/', views.ContentDetailView.as_view(), name='content_detail'),
    path('create/', views.ContentCreateView.as_view(), name='content_create'),
    path('update/<int:pk>/', views.ContentUpdateView.as_view(), name='content_update'),
]