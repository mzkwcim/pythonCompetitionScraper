import time
from app.records.records_table import RecordsTablesGroup
from app.loader.config_loader import config
from app.service.orchestrator import Orchestrator
from app.io.serializer import Serializer

class Ranking:
    @staticmethod
    def populate_records(save: bool = True) -> RecordsTablesGroup:
        records = RecordsTablesGroup()
        for gender in config['genders'].values():
            for course in config['courses'].values():
                for age, group in config['age_groups'].items():
                    Orchestrator.handle_single_table(gender, course, age, group, records)
                    time.sleep(config["pause_time"])
        if save:
            Serializer.save_records_to_json(records)
        return records
    
    
            