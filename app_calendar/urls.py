from django.urls import path

from app_calendar import views

urlpatterns = [
    path('list_event', views.ListEvent.as_view()),
    path('create_event', views.CreateEvent.as_view()),

]