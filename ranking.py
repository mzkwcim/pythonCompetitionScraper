import requests
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time

def map_age_group_to_string(age_group):
    print()

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

records = {}
genders = config['genders']
courses = config['courses']
age_groups = config['age_groups']
for gender in genders:
    for course in courses:
        for age, group in age_groups.items():
            url = f"{config['base_url']}?page=rankingDetail&clubId=65773&gender={gender}&course={course}&agegroup={age}&season=-1"
            records_name = f"Rekordy {"zawodników" if gender == "1" else "zawodniczek"} {group} na basenie {"25 metrowym" if course == "SCM" else "50 metrowym"}"
            print(url)
            print(records_name)
            print(gender)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            regex_pattern = r'<select\s+(?:[^>]*?\s+)?name=["\']agegroup["\'](?:\s+[^>]*?)?>(.*?)</select>'
            match = re.search(regex_pattern, str(soup), re.DOTALL | re.IGNORECASE)
            full_select_element = match.group(0)
            options_content = match.group(1)
            print(full_select_element)
            print(options_content)
            selected_option_regex = r'<option\s+(?:[^>]*?\s+)?value=["\']([^"\']*)["\'](?:\s+[^>]*?)?\s+selected=["\']?["\']?(?:\s+[^>]*?)?>(.*?)</option>'
            selected_option_match = re.search(selected_option_regex, options_content, re.DOTALL | re.IGNORECASE)
            value = selected_option_match.group(1)
            print(value)
            age_group_select = ""
            # print(age_group_select)
            print("siema")
            time.sleep(10)
            selected_option = age_group_select.find('option', selected=True)
            print(selected_option)
            time.sleep(10)
            tables = soup.find('table', class_='rankingList')
            events = tables.find_all('td', class_='swimstyle')
            yob = tables.find_all('td', class_='rankingPlace')[::2]
            date = tables.find_all('td', class_='date')
            print(f"{int(str(date[0].decode_contents()).replace("\u00a0"," ").split(" ")[-1])} - {int(str(yob[0].decode_contents()))} == {int(age)}")
            check = int(str(date[0].decode_contents()).replace("\u00a0"," ").split(" ")[-1]) - int(str(yob[0].decode_contents())) == int(age)
            print(check)
            time.sleep(10)
            for event in events:
                print(event.decode_contents())
            time.sleep(30)
            athlete_name = tables.find_all('td', class_='fullname')
            swim_time = tables.find_all('td', class_='time')
            date = tables.find_all('td', class_='date')
            city = tables.find_all('td', class_='city')
            
            
            