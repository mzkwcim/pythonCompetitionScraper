import bs4

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