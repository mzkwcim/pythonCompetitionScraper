import requests
from bs4 import BeautifulSoup
base_url = "https://www.swimrankings.net/index.php"
url = f"{base_url}?page=rankingDetail&clubId=65773&gender=1&season=2025&agegroup=0&stroke=9"  
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find_all(class_='athleteList')
athlete_max_points = {}
for table in tables:
    athlete_list = table.find_all('td', class_='name')
    for athlete_obj in athlete_list:
        athlete = athlete_obj.find('a')
        athlete_url = f"{base_url}{athlete.get('href')}"
        
        athlete_name = str(athlete.decode_contents()).replace(",","").title()
        athlete_response = requests.get(athlete_url)
        athlete_soup = BeautifulSoup(athlete_response.text, 'html.parser')
        athlete_points = athlete_soup.find_all('td', class_='code')
        max_points = 0
        for point in athlete_points:
            current_points = point.decode_contents()
            if current_points == "-":
                continue
            current_points = int(current_points)
            if max_points < current_points:
                max_points = current_points
        athlete_max_points[athlete_name] = max_points
        
for k,v in athlete_max_points.items():
    print(f"{k}: {v}")
