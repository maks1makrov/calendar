from rest_framework.serializers import ModelSerializer

from app_calendar.models import Event


class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = ('user', 'title', 'start_date', 'end_date')