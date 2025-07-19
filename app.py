from flask import Flask, render_template
from app.records.records_table import RecordsTablesGroup
from app.ranking.ranking import Ranking
from app.io.serializer import Serializer
from app.loader.config_loader import config
from app.service.repair import Repair

app = Flask(__name__)
records = Serializer.load_records_from_json()

Repair.repair_missing_events(records, config)

Serializer.save_records_to_json(records)

for course in config["courses"].keys():
    for gender in config["genders"].keys():
        grouped_names = records.group_records(gender, course)

        previous_table = records.get_table(grouped_names[0])
        previous_events = previous_table.get_events()
        previous_times = previous_table.get_decimal_records()

        # for name in grouped_names[1:]:
