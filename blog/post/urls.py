from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_post, name='create_post'),
    path('view/<int:post_id>/', views.view_post, name='view_post'),
]