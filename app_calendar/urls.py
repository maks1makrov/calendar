from django.urls import path

from app_calendar import views

urlpatterns = [
    path('list_event', views.ListEvent.as_view()),
    path('list_event/<int:year>/<int:month>', views.ListEvent_month.as_view()),
    path('create_event', views.CreateEvent.as_view()),
    path('list_holidays', views.ListHolidays.as_view()),
    path('list_holidays/<int:year>/<int:month>', views.ListHolidays_month.as_view()),


]