from app.records.records_table import RecordsTablesGroup
from app.loader.config_loader import config
from app.io.serializer import Serializer


class Repair:
    @staticmethod               
    def reparir_records(records: RecordsTablesGroup) -> None:
        for course in config["courses"].keys():
            for gender in config["genders"].keys():
                grouped_names = records.group_records(gender, course)

                for i in range(1, len(grouped_names)):
                    younger_group_name = grouped_names[i-1]
                    older_group_name = grouped_names[i]

                    younger_table = records.get_table(younger_group_name)
                    older_table = records.get_table(older_group_name)

                    print(f"\n--- Comparing {younger_group_name} (younger) with {older_group_name} (older) ---")

                    events_to_check = younger_table.get_events()

                    for event_key in events_to_check:
                        younger_record_data = younger_table.get_record(event_key)
                        if not younger_record_data: 
                            continue

                        y_event, y_athlete, y_readable_time, y_decimal_time, y_city, y_competition_date = younger_record_data

                        older_record_data = older_table.get_record(event_key)
                        if older_record_data == None:
                            older_table.add_record(y_event, y_athlete, y_readable_time, y_decimal_time, y_city, y_competition_date)
                            continue

                        if not older_record_data or y_decimal_time < older_record_data[3]: 
                            o_event, o_athlete, o_readable_time, o_decimal_time, o_city, o_competition_date = older_record_data if older_record_data else (None, "Brak rekordu", "N/A", float('inf'), None, None)

                            print(f"Potential update for {event_key}:")
                            print(f"  Younger athlete ({younger_group_name}): {y_athlete} - {y_readable_time}")
                            print(f"  Older athlete ({older_group_name}): {o_athlete} - {o_readable_time}")

                            older_table.update_record(
                                event_key,          
                                y_athlete,         
                                y_readable_time,    
                                y_decimal_time,    
                                y_city,            
                                y_competition_date  
                            )
                            print(f"  -> Updated {older_group_name} record for {event_key} with {y_athlete}'s time: {y_readable_time}")
                        else:
                            pass


        print("\n--- All comparisons complete. ---")
        print("Remember to uncomment `Serializer.save_records_to_json(records)` to save changes.")
        Serializer.save_records_to_json(records)
                        
