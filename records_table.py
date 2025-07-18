class RecordTable:
    def __init__(self, name: str):
        self.name = name
        self.records = {
            "event": [],
            "athlete": [],
            "readable_time": [],
            "decimal_time": [],
            "city": [],
            "competition_date": []
        }
        
    def add_record(
        self, 
        event: str, 
        athlete_name: str, 
        readable_time: str, 
        decimal_time: float, 
        competition_date: str, 
        city: str
    ) -> None:
        self.records["event"].append(event)
        self.records["athlete"].append(athlete_name)
        self.records["readable_time"].append(readable_time)
        self.records["decimal_time"].append(decimal_time)
        self.records["city"].append(city)
        self.records["competition_date"].append(competition_date)
        
    def get_records(self):
        return self.records
    
class RecordsTablesGroup:
    def __init__(self):
        self.tables = {}
        
    def add_table(self, name: str):
        self.tables[name] = RecordTable(name)
        
    def get_table(self, name: str) -> RecordTable:
        return self.tables[name]
    
    def get_all_tables(self):
        return self.tables.values()