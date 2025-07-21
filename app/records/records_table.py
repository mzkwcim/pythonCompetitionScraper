from enum import Enum

class Strokes(Enum):
    MOTYLKOWYM = "motylkowym"
    GRZBIETOWYM = "grzbietowym"
    KLASYCZNYM = "klasycnzym"
    DOWOLNYM = "dowolnym"
    ZMIENNYM = "zmiennym"
    
class Distance(Enum):
    M_50 = "50m"
    M_100 = "100m"
    M_200 = "200m"
    M_400 = "400m"
    M_800 = "800m"
    M_1500 = "1500m"

class RecordTable:
    def __init__(self, name: str) -> None:
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
        
    def update_record(
        self, 
        event: str, 
        athlete_name: str, 
        readable_time: str, 
        decimal_time: float, 
        competition_date: str, 
        city: str
    ) -> None:
        index = self._get_index_of_event(event)
        self.records["event"][index] = event
        self.records["athlete"][index] = athlete_name
        self.records["readable_time"][index] = readable_time
        self.records["decimal_time"][index] = decimal_time
        self.records["city"][index] = city
        self.records["competition_date"][index] = competition_date
        
    def get_records_per_style(self, stroke: Strokes):
        return [name for name in self.records["event"] if stroke.value in name]
    
    def get_records_per_distance(self, distance: Distance):
        return [name for name in self.records["event"] if distance.value in name]
        
    def get_events(self) -> list[str]:
        return self.records["event"]
    
    def get_decimal_records(self) -> list[float]:
        return self.records["decimal_time"]
        
    def get_records(self) -> dict[str, list]:
        return self.records
    
    def get_record(self, event: str) -> tuple[str, str, str, float, str, str]:
        index = self._get_index_of_event(event)
        return (
            self.records["event"][index],
            self.records["athlete"][index],
            self.records["readable_time"][index],
            self.records["decimal_time"][index],
            self.records["city"][index],
            self.records["competition_date"][index]
        )
    
    def _get_index_of_event(self, event: str) -> int:
        return self.records["event"].index(event)
        
class RecordsTablesGroup:
    def __init__(self) -> None:
        self.tables = {}
        
    def add_table(self, name: str) -> None:
        self.tables[name] = RecordTable(name)
        
    def get_table(self, name: str) -> RecordTable:
        return self.tables[name]
    
    def get_all_tables_names(self) -> list[str]:
        return list(self.tables.keys())
    
    def get_all_tables(self)-> list[RecordTable]:
        return self.tables.values()
    
    def add_existing_table(self, table: RecordTable) -> None:
        self.tables[table.name] = table
        
    def group_records(self, gender: str, course: str) -> list[str]:
        return [name for name in self.tables if gender in name and course in name]