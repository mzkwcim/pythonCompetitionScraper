import time
from records_table import RecordsTablesGroup
from config_loader import config
from scraping.orchestrator import Orchestrator

records = RecordsTablesGroup()

for gender in config['genders']:
    for course in config['courses']:
        for age, group in config['age_groups'].items():
            Orchestrator.handle_single_table(gender, course, age, group, records)
            time.sleep(10)
            
            
            