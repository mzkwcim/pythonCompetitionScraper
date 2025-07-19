import json
from app.records.records_table import RecordsTablesGroup, RecordTable

class Serializer:
    @staticmethod
    def save_records_to_json(records: RecordsTablesGroup, filepath: str = "rankings.json") -> None:
        data = {}
        for name, table in records.tables.items():
            data[name] = table.get_records()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    @staticmethod
    def load_records_from_json(filepath: str = "rankings.json") -> RecordsTablesGroup:
        records_group = RecordsTablesGroup()

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        for name, record_data in data.items():
            table = RecordTable(name)
            table.records = record_data  
            records_group.add_existing_table(table)

        return records_group