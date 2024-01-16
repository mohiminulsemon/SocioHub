from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post_details/<int:post_id>/', views.post_details, name='post_details'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('toggle_edit_comment/<int:comment_id>/', views.toggle_edit_comment, name='toggle_edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),

]
