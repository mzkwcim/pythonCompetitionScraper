from flask import Flask, render_template
from app.records.records_table import RecordsTablesGroup
from app.ranking.ranking import Ranking
from app.io.serializer import Serializer
from app.loader.config_loader import config
from app.service.repair import Repair
import time

app = Flask(__name__)
records = Serializer.load_records_from_json()

# Repair.repair_missing_events(records, config)

# Serializer.save_records_to_json(records)

for course in config["courses"].keys():
    for gender in config["genders"].keys():
        grouped_names = records.group_records(gender, course)

        previous_table = records.get_table(grouped_names[0])
        previous_events = previous_table.get_events()
        previous_times = previous_table.get_decimal_records()

        for name in grouped_names[1:]:
            current_table = records.get_table(name)
            current_events = current_table.get_events()
            current_times = current_table.get_decimal_records()
            for index, _ in enumerate(previous_events):
                print(f"Previous event and time {previous_events[index]} {previous_times[index]} {previous_table[index]}")
                print(f"Current event and time {current_events[index]} {current_times[index]} {current_table[index]}")
                time.sleep(10)
            
