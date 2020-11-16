from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from app_calendar.models import Event
from app_calendar.serializer import EventSerializer


class CreateEvent(CreateAPIView):

    serializer_class = EventSerializer

class ListEvent(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()