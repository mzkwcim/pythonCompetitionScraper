import json
import bs4

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

def translate_stroke(distance: str) -> str:
    distance_split = distance.split(" ")
    return f"{distance_split[0]} {config['styles'][distance_split[-1]]}"
        
def translate_date(date: bs4.element.Tag) -> str:
    date = str(date.find(text=True, recursive=False)).strip()
    date_list = date.split("\u00a0")
    return f"{date_list[0]} {config['months'][date_list[1]]} {date_list[2]}"

def translate_age_to_category(age: int) -> str:
    match age:
        case _ if age <= 11:
            return "Dziecko"
        case _ if age > 11 and age <= 13:
            return "Mlodzik"
        case _ if age > 13 and age <= 16:
            return "Junior Mlodszy"
        case _ if age > 16 and age <= 18:
            return "Junior"
        case _ if age > 18 and age <= 23:
            return "Mlodzieżowiec"
        case _ if age > 23:
            return "Senior"
        
def check_site_correctness(dates: list, yobs: list, age: str) -> bool:
    return int(str(dates[0].decode_contents()).replace("\u00a0"," ").split(" ")[-1]) - int(str(yobs[0].decode_contents())) == int(age[0:2])

def get_record_name(gender: str, group: str, course: str) -> str:
    return f"Rekordy {"zawodników" if gender == "1" else "zawodniczek"} {group} na basenie {"25 metrowym" if course == "SCM" else "50 metrowym"}"

def create_url(gender: str, course: str, age: str) -> str:
    return f"{config['base_url']}?page=rankingDetail&clubId={config['clubId']}&gender={gender}&course={course}&agegroup={age}&season=-1"

def format_athlete_name(athlete_element: bs4) -> str:
    return str(athlete_element.find('a').find(text=True, recursive=False)).replace(",", "").title()

def format_string_time(swim_time_element: bs4) -> str:
    return str(swim_time_element.find('a').find(text=True, recursive=False))

def format_city(city_element: bs4) -> str:
    return str(city_element.find('a').decode_contents())

def format_decimal_time(string_time: str) -> float:
    splited_time = string_time.split(":")
    return float((int(splited_time[0])*60) + float(splited_time[1])) if len(splited_time) > 1 else float(splited_time[0])