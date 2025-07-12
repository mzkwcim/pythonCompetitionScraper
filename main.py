import requests
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


clubId = 65773
year = 2025
stroke = 8
courses = ['LCM', 'SCM']
meetings = {}
base_url = "https://www.swimrankings.net/index.php"
ranking_details = "page=rankingDetail"
regex_class = re.compile(r"^meetResult[0-1]$")
current_year = datetime.now().year
counter = 0
athlete_name = ""
for course in courses:
    url = f"{base_url}?{ranking_details}&clubId={clubId}&stroke={stroke}&year={year}&course={course}"  
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    elements_td = soup.find_all('td', class_='name')
    for element_td in elements_td:
        counter += 1
        link_element = element_td.find('a')
        if link_element:
            meeting_url = f"{base_url}{link_element.get('href')}&clubId={clubId}"
            meeting_response = requests.get(meeting_url)
            meeting_html_content = meeting_response.text
            meeting_soup = BeautifulSoup(meeting_html_content, 'html.parser')
            meeting_name = meeting_soup.find('td', class_='titleLeft').decode_contents()
            meeting_city = meeting_soup.find_all('td', class_='titleLeft')[1].decode_contents().replace("\u00a0"," ").replace("\u00a0", " ")
            meeting_date = meeting_soup.find_all('td', class_='titleRight')[1].decode_contents().replace("\u00a0"," ").replace("\u00a0", " ")
            meetings[meeting_name] = {
                "city": meeting_city,
                "date": meeting_date
            }
            
            meeting_elements = meeting_soup.find_all('tr', class_=regex_class)
            for meeting_element in meeting_elements:
                meeting_class = meeting_element.get('class')[0]
                if meeting_class:
                    if meeting_class == "meetResult1":
                        athlete_element = meeting_element.find('td', class_='nameImportant')
                        if athlete_element:
                            athlete_name = str(athlete_element.find('a').decode_contents()).replace(",","").title()
                            print(athlete_name)
                            athlete_birth = int(current_year) - int(str(athlete_element.decode_contents().split(" - ")[-1]).strip())
                            meetings[meeting_name][athlete_name] = {
                                "age": athlete_birth,
                            }
                    elif meeting_class == "meetResult0":
                        distance_element = meeting_element.find('td', class_='name').find('a').decode_contents()
                        place_element = str(meeting_element.find('td', class_='meetPlace').decode_contents().split(" ")[-1])
                        if "Split" in place_element or "DSQ" in place_element or "4 x " in distance_element:
                            continue
                        place = place_element.replace(".","")
                        if "swimmingEvents" not in meetings[meeting_name][athlete_name]:
                            meetings[meeting_name][athlete_name]["swimmingEvents"] = {}

                        meetings[meeting_name][athlete_name]["swimmingEvents"][distance_element] = place
                        print(distance_element)
                        print(place)
                        print(json.dumps(meetings, indent=4))
                        

last_col_index = (counter + 1) * 3
last_col_letter = get_column_letter(last_col_index)                       
wb = Workbook()
ws = wb.active
ws.merge_cells(f"A1:{last_col_letter}1")
ws.merge_cells(f"A2:{last_col_letter}2")
ws.merge_cells(f"B3:{last_col_letter}3")
ws["A1"] = f"UCZESTNICTWO W ZAWODACH OBJĘTYCH SYSTEMEM WSPÓŁZAWODNICTWA SPORTOWEGO W {current_year} ROKU"
ws["A2"] = f"Nazwa klubu: Ks Posnania Poznan"
ws["A3"] = f"Dyscyplina: PŁYWANIE"
ws.merge_cells("A4:A7")
ws.merge_cells("B4:B7")
ws.merge_cells("C4:C7")
ws["A4"] = "L.p. (*)"
ws["B4"] = "Imię i nazwisko zawodnika objętego szkoleniem w 2024 roku"
ws["C4"] = "Kategoria wiekowa"


# print(json.dumps(meetings, indent=4))
    


