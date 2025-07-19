from flask import Flask, render_template
from records_table import RecordsTablesGroup

app = Flask(__name__)
records = RecordsTablesGroup()