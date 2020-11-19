from django.urls import path
from knox import views as knox_views
from app_auth import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),


]