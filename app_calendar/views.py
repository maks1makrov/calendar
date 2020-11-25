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
    def get_queryset(self):
        print(self.request.user)
        return Event.objects.filter(user=self.request.user.id)


class ListHolidays(ListAPIView):
    serializer_class = HolidaySerializer
    # queryset = Event.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # print(self.request.user)
        return Holiday.objects.filter(country=self.request.user.country)