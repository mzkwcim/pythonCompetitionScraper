import requests
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime


clubId = 65773
year = 2025
stroke = 8
courses = ['LCM', 'SCM']
meetings = {}
base_url = "https://www.swimrankings.net/index.php"
ranking_details = "page=rankingDetail"
regex_class = re.compile(r"^meetResult[0-1]$")
current_year = datetime.now().year

for course in courses:
    url = f"{base_url}?{ranking_details}&clubId={clubId}&stroke={stroke}&year={year}&course={course}"  
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    elements_td = soup.find_all('td', class_='name')
    for element_td in elements_td:
        link_element = element_td.find('a')
        if link_element:
            meeting_url = f"{base_url}{link_element.get('href')}&clubId={clubId}"
            meeting_response = requests.get(meeting_url)
            meeting_html_content = meeting_response.text
            meeting_soup = BeautifulSoup(meeting_html_content, 'html.parser')
            meeting_name = meeting_soup.find('td', class_='titleLeft').decode_contents()
            meeting_city = meeting_soup.find_all('td', class_='titleLeft')[1].decode_contents()
            meeting_date = meeting_soup.find_all('td', class_='titleRight')[1].decode_contents()
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
                            athlete_birth = int(current_year) - int(str(athlete_element.decode_contents().split(" - ")[-1]).strip())
                            meetings[meeting_name][athlete_name] = {
                                "age": athlete_birth,
                            }
                    # elif meeting_class == "meetResult0":
                        

                        
            
print(json.dumps(meetings, indent=4))
    


