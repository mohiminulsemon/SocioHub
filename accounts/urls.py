from django.urls import path
from . import views

urlpatterns = [
    path('activate/<uid64>/<token>/', views.activate, name='activate'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.UserProfileUpdateView.as_view(), name='update_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('changePassword/', views.change_password, name='changePassword'),
    path('changePassword2/', views.change_password2, name='changePassword2'),

]