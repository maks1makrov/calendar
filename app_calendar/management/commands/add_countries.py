from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
import requests
from tqdm import tqdm
from app_calendar.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "https://www.officeholidays.com/countries"
        req = requests.get(url).text
        bs = BeautifulSoup(req)
        bs_3_colums = bs.find_all("div", {"class":"four omega columns"})
        arr = []
        for i in bs_3_colums:
            colum = i.find_all('a')
            for country in colum:
                arr.append(country.text.strip())
        for country in tqdm(arr):
            Country.objects.create(country=country)
