from app.records.records_table import RecordsTablesGroup
from app.scraping.parser import Parser
from app.scraping.fetch import Fetcher
from app.helpers.utils import Utils

class Orchestrator:
    @staticmethod
    def handle_single_table(gender: str, course: str, age: str, group: str, records: RecordsTablesGroup) -> None:
        url = Utils.create_url(gender, course, age)
        records_name = Utils.get_record_name(gender, group, course)
        records.add_table(records_name)
        record = records.get_table(records_name)
        soup = Fetcher.fetch_soup(url)
        data = Parser.parse_table_data(soup)

        if not Utils.check_site_correctness(data["dates"], data["yobs"], age):
            print(f"skipuję {url} nieprawidłowa data urodzenia")
            return

        for i, _ in enumerate(data["events"]):
            Parser.process_event(i, data, record)
        print(record.get_records())