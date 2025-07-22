from flask import Flask, render_template
from app.records.records_table import RecordsTablesGroup
from app.ranking.ranking import Ranking
from app.io.serializer import Serializer
from app.loader.config_loader import config
from app.service.repair import Repair
from app.records.records_table import Strokes, Distance
import time

app = Flask(__name__)
records = Serializer.load_records_from_json()

# Repair.repair_missing_events(records, config)

# Serializer.save_records_to_json(records)

for course in config["courses"].keys():
    for gender in config["genders"].keys():
        grouped_names = records.group_records(gender, course)

        previous_table = records.get_table(grouped_names[0])
        print(previous_table.get_records_per_style(Strokes.DOWOLNYM))
        print(previous_table.get_records_per_distance(Distance.M_100))
        previous_events = previous_table.get_events()
        previous_times = previous_table.get_decimal_records()

        for name in grouped_names[1:]:
            current_table = records.get_table(name)
            current_events = current_table.get_events()
            current_times = current_table.get_decimal_records()
            for index, _ in enumerate(previous_events):
                previous_event = previous_events[index]
                current_event = previous_table.get_record(previous_event)[0]
                previous_time = previous_times[index]
                current_time = current_times[index]
                if previous_time < current_time:
                    event, athlete, readale_time, decimal_time, city, competition_date = previous_table.get_record(previous_event)
                    c_event, c_athlete, c_readable_time, c_decimal_time, c_city, c_competition_date = current_table.get_record(previous_event)
                    print(f"Younger athlete {athlete} had better time than older athlete {c_athlete} on {c_event}, time comparison:\n older: {c_readable_time}\n younger {readale_time}")
                    # current_table.update_record(event, athlete, readale_time, decimal_time, city, competition_date)
                previous_table = current_table
            
                
            
