from app.loader.config_loader import config
from app.helpers.formater import Formater
import bs4

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