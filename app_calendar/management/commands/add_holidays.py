from django.core.management import BaseCommand
from ics import Calendar
import requests
from tqdm import tqdm
from app_calendar.models import Holiday, Country


# class Command(BaseCommand):
#
#     def handle(self, *args, **kwargs):
#         for country in tqdm(Country.objects.all()):
#             url = f"https://www.officeholidays.com/ics/ics_country.php?tbl_country={country}"
#             res = requests.get(url).text
#             try:
#                 calendar = Calendar(res)
#                 events_cal = calendar.events
#                 for added_holidays in events_cal:
#                     Holiday.objects.create(
#                         title=added_holidays.name,
#                         date=added_holidays.begin.date(),
#                         country=Country.objects.get(name=added_holidays.location))
#             except:
#                 pass


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # for country in tqdm(Country.objects.all()):
        url = f"https://www.officeholidays.com/ics/ics_country.php?tbl_country=Belarus"
        res = requests.get(url).text
        try:
            calendar = Calendar(res)
            events_cal = calendar.events
            for added_holidays in events_cal:
                Holiday.objects.create(
                    title=added_holidays.name,
                    date=added_holidays.begin.date(),
                    country=Country.objects.get(country=added_holidays.location))
        except:
            pass