from app.records.records_table import RecordsTablesGroup


class Repair:
    @staticmethod
    def repair_missing_events(records: RecordsTablesGroup, config: dict) -> None:
        for course in config["courses"].keys():
            for gender in config["genders"].keys():
                grouped_names = records.group_records(gender, course)

                previous_table = records.get_table(grouped_names[0])
                previous_events = previous_table.get_events()

                for name in grouped_names[1:]:
                    current_table = records.get_table(name)
                    current_events = current_table.get_events()

                    missing_elements = set(previous_events) - set(current_events)
                    for missing_event in missing_elements:
                        record = previous_table.get_record(missing_event)
                        current_table.add_record(record)
                        
