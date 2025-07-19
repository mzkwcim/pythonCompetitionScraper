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
        
    def get_events(self) -> list[str]:
        return self.records["event"]
    
    def get_decimal_records(self) -> list[float]:
        return self.records["decimal_time"]
        
    def get_records(self):
        return self.records
    
    def get_record(self, index: int) -> tuple[str, str, str, float, str, str]:
        return (
            self.records["event"][index],
            self.records["athlete"][index],
            self.records["readable_time"][index],
            self.records["decimal_time"][index],
            self.records["city"][index],
            self.records["competition_date"][index]
        )
    
    def get_index_of_event(self, event: str):
        return self.records["event"].index(event)
    
class RecordsTablesGroup:
    def __init__(self):
        self.tables = {}
        
    def add_table(self, name: str):
        self.tables[name] = RecordTable(name)
        
    def get_table(self, name: str) -> RecordTable:
        return self.tables[name]
    
    def get_all_tables_names(self) -> list[str]:
        return list(self.tables.keys())
    
    def get_all_tables(self):
        return self.tables.values()
    
    def add_existing_table(self, table: RecordTable):
        self.tables[table.name] = table
        
    def group_records(self, gender: str, course: str) -> list[str]:
        return [name for name in self.tables if gender in name and course in name]