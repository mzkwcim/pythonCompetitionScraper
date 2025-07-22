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
Repair.reparir_records(records)


            
