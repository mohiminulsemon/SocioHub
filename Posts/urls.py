from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),


]
