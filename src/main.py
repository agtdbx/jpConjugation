from parsing.load import load_json_file
from parsing.verbe import parse_conjugation_data
from verbes.present import  get_present_godan_formes, \
                            get_present_ichidan_formes, \
                            get_present_exception_formes
from verbes.passe import    get_passe_godan_formes, \
                            get_passe_ichidan_formes, \
                            get_passe_exception_formes

if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/data.json")