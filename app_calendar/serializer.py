from rest_framework.serializers import ModelSerializer

from app_calendar.models import Event, Holiday


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ('user', 'title', 'start_date', 'end_date')

class HolidaySerializer(ModelSerializer):

    class Meta:
        model = Holiday
        fields = ('title', 'date', 'country')