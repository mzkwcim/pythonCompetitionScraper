import requests
import json
from bs4 import BeautifulSoup
import time
from helper import translate_date, translate_stroke, check_site_correctness, get_record_name, create_url, format_athlete_name, format_string_time, format_city, format_decimal_time

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

records = {}
genders = config['genders']
courses = config['courses']
age_groups = config['age_groups']
for gender in genders:
    for course in courses:
        for age, group in age_groups.items():
            url = create_url(gender, course, age)
            records_name = get_record_name(gender, group, course)
            print(url)
            print(records_name)
            print(gender)
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
            if not check_site_correctness(dates, yobs, age):
                print(f"skipuję {url} nieprawidłowa data urodzenia")
                continue
            for index, event in enumerate(events):
                decoded_event = events[index].find('a').decode_contents()
                if "Lap" in decoded_event:
                    break
                decoded_event = translate_stroke(decoded_event)
                decoded_athlete_name = format_athlete_name(athlete_names[index])
                decoded_date = translate_date(dates[index])
                decoded_cities = format_city(cities[index])
                decoded_time = format_string_time(swim_times[index])
                decimal_time = format_decimal_time(decoded_time)
                
                print(f"{decoded_event}: {decoded_athlete_name} {decoded_date} {decoded_cities} {decoded_time} {decimal_time}")
            time.sleep(10)
            
            
            