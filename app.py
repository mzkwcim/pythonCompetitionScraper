from flask import Flask, render_template, redirect, url_for, request
from app.records.records_table import RecordsTablesGroup
from app.ranking.ranking import Ranking
from app.io.serializer import Serializer
from app.loader.config_loader import config
from app.service.repair import Repair
from app.records.records_table import Strokes, Distance
import time
import requests

# records = Ranking.populate_records()
# Repair.reparir_records(records)
# Serializer.save_records_to_json(records)
# records = Serializer.load_records_from_json()
# Repair.reparir_records(records)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/login.html")

@app.route("/hello/<name>")
def hello(name):
    return "Hello %s!" %name

@app.route("/success/<name>")
def success(name):
    return "Welcome %s!" %name

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for('success', name=user))
    elif request.method == "GET":
        user = request.args.get("nm")
        return redirect(url_for('success', name=user))
    


if __name__ == "__main__":
    app.run()



            
