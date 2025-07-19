from flask import Flask, render_template
from app.records.records_table import RecordsTablesGroup
from app.ranking.ranking import Ranking

app = Flask(__name__)
records = Ranking.populate_records(read_from_json=False, save=True)
print(records)