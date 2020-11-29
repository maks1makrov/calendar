from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView

from app_calendar.models import Event, Holiday
from app_calendar.serializer import EventSerializer, HolidaySerializer


class CreateEvent(CreateAPIView):

    serializer_class = EventSerializer

class ListEvent(ListAPIView):
    serializer_class = EventSerializer
    # queryset = Event.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['start_date']
    def get_queryset(self):
        print(self.request.user)
        return Event.objects.filter(user=self.request.user.id)


class ListEvent_month(ListAPIView):
    serializer_class = EventSerializer
    # queryset = Event.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['start_date']
    def get_queryset(self):
        print(self.request.user)
        return Event.objects.filter(user=self.request.user.id, start_date__year=self.kwargs['year'], start_date__month=self.kwargs['month'])

class ListHolidays(ListAPIView):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['date']
    def get_queryset(self):
        # print(self.request.user)
        return Holiday.objects.filter(country=self.request.user.country)


class ListHolidays_month(ListAPIView):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['date']
    def get_queryset(self):
        # print(self.request.user)
        return Holiday.objects.filter(country=self.request.user.country, date__year=self.kwargs['year'], date__month=self.kwargs['month'])