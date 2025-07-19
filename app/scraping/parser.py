from bs4 import BeautifulSoup
from app.records.records_table import RecordTable
from app.helpers.translator import Translator
from app.helpers.formater import Formater

class Parser:
    @staticmethod
    def parse_table_data(soup: BeautifulSoup) -> dict:
        table = soup.find('table', class_='rankingList')
        return {
            "events": table.find_all('td', class_='swimstyle'),
            "yobs": table.find_all('td', class_='rankingPlace')[::2],
            "dates": table.find_all('td', class_='date'),
            "athlete_names": table.find_all('td', class_='fullname'),
            "swim_times": table.find_all('td', class_='time'),
            "cities": table.find_all('td', class_='city')
        }
        
    @staticmethod
    def process_event(index: int, data: dict, record: RecordTable) -> None:
        decoded_event = data["events"][index].find('a').decode_contents()
        if "Lap" in decoded_event:
            return
        decoded_event = Translator.translate_stroke(decoded_event)
        decoded_name = Formater.format_athlete_name(data["athlete_names"][index])
        decoded_date = Translator.translate_date(data["dates"][index])
        decoded_city = Formater.format_city(data["cities"][index])
        decoded_time = Formater.format_string_time(data["swim_times"][index])
        decimal_time = Formater.format_decimal_time(decoded_time)
        record.add_record(decoded_event, decoded_name, decoded_time, decimal_time, decoded_date, decoded_city)   