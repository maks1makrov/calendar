from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_data = models.DateTimeField(default=start_date)