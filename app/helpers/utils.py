from app.loader.config_loader import config

class Utils:
    @staticmethod
    def check_site_correctness(dates: list, yobs: list, age: str) -> bool:
        return int(str(dates[0].decode_contents()).replace("\u00a0"," ").split(" ")[-1]) - int(str(yobs[0].decode_contents())) == int(age[0:2])

    @staticmethod
    def get_record_name(gender: str, group: str, course: str) -> str:
        return f"Rekordy {"zawodników" if gender == "1" else "zawodniczek"} {group} na basenie {"25 metrowym" if course == "SCM" else "50 metrowym"}"

    @staticmethod
    def create_url(gender: str, course: str, age: str) -> str:
        return f"{config['base_url']}?page=rankingDetail&clubId={config['clubId']}&gender={gender}&course={course}&agegroup={age}&season=-1&language=pl"
    