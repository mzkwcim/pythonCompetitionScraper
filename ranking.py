import requests
import json
from bs4 import BeautifulSoup
import time
from helper import Translator, Formater, Utils
from records_table import RecordsTablesGroup, RecordTable
from config_loader import config

records = {}
genders = config['genders']
courses = config['courses']
age_groups = config['age_groups']
for gender in genders:
    for course in courses:
        for age, group in age_groups.items():
            url = Utils.create_url(gender, course, age)
            records_name = Utils.get_record_name(gender, group, course)
            record = RecordTable(records_name)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            tables = soup.find('table', class_='rankingList')
            events = tables.find_all('td', class_='swimstyle')
            yobs = tables.find_all('td', class_='rankingPlace')[::2]
            dates = tables.find_all('td', class_='date')
            athlete_names = tables.find_all('td', class_='fullname')
            swim_times = tables.find_all('td', class_='time')
            dates = tables.find_all('td', class_='date')
            cities = tables.find_all('td', class_='city')
            if not Utils.check_site_correctness(dates, yobs, age):
                print(f"skipuję {url} nieprawidłowa data urodzenia")
                continue
            for index, event in enumerate(events):
                decoded_event = events[index].find('a').decode_contents()
                if "Lap" in decoded_event:
                    break
                decoded_event = Translator.translate_stroke(decoded_event)
                decoded_athlete_name = Formater.format_athlete_name(athlete_names[index])
                decoded_date = Translator.translate_date(dates[index])
                decoded_cities = Formater.format_city(cities[index])
                decoded_time = Formater.format_string_time(swim_times[index])
                decimal_time = Formater.format_decimal_time(decoded_time)
                record.add_record(decoded_event, decoded_athlete_name, decoded_time, decimal_time, decoded_date, decoded_cities)
            print(record.ger_records())
            time.sleep(10)
            
            
            