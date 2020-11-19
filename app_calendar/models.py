
from django.db import models
from knox.auth import User


class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


# class User(AbstractUser):
#     country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()