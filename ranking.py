import time
from records.records_table import RecordsTablesGroup
from config_loader import config
from app.service.orchestrator import Orchestrator
from app.io.serializer import Serializer

class Ranking:
    @staticmethod
    def populate_records(read_from_json: bool, save: bool = True) -> RecordsTablesGroup:
        if read_from_json:
            records =  Serializer.load_records_from_json()
            return records
        records = RecordsTablesGroup()
        for gender in config['genders']:
            for course in config['courses']:
                for age, group in config['age_groups'].items():
                    Orchestrator.handle_single_table(gender, course, age, group, records)
                    time.sleep(10)
        if save:
            Serializer.save_records_to_json(records)
        return records
            