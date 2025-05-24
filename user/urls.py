from django.urls import path
from user import views


urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]
