import bs4
from config_loader import config

class Translator:
    @staticmethod
    def translate_stroke(distance: str) -> str:
        distance_split = distance.split(" ")
        return f"{distance_split[0]} {config['styles'][distance_split[-1]]}"
            
    @staticmethod
    def translate_date(date: bs4) -> str:
        date_list = Formater.format_date(date)
        return f"{date_list[0]} {config['months'][date_list[1]]} {date_list[2]}"

    @staticmethod
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
        
        
class Utils:
    @staticmethod
    def check_site_correctness(dates: list, yobs: list, age: str) -> bool:
        return int(str(dates[0].decode_contents()).replace("\u00a0"," ").split(" ")[-1]) - int(str(yobs[0].decode_contents())) == int(age[0:2])

    @staticmethod
    def get_record_name(gender: str, group: str, course: str) -> str:
        return f"Rekordy {"zawodników" if gender == "1" else "zawodniczek"} {group} na basenie {"25 metrowym" if course == "SCM" else "50 metrowym"}"

    @staticmethod
    def create_url(gender: str, course: str, age: str) -> str:
        return f"{config['base_url']}?page=rankingDetail&clubId={config['clubId']}&gender={gender}&course={course}&agegroup={age}&season=-1"
    
    
class Formater:
    @staticmethod
    def format_date(competition_date: bs4) -> list:
        date = str(competition_date.find(text=True, recursive=False)).strip()
        date_list = date.split("\u00a0")
        return date_list
    
    @staticmethod
    def format_athlete_name(athlete_element: bs4) -> str:
        return str(athlete_element.find('a').find(text=True, recursive=False)).replace(",", "").title()
    
    @staticmethod
    def format_string_time(swim_time_element: bs4) -> str:
        return str(swim_time_element.find('a').find(text=True, recursive=False))

    @staticmethod
    def format_city(city_element: bs4) -> str:
        return str(city_element.find('a').decode_contents())

    @staticmethod
    def format_decimal_time(string_time: str) -> float:
        splited_time = string_time.split(":")
        return float((int(splited_time[0])*60) + float(splited_time[1])) if len(splited_time) > 1 else float(splited_time[0])