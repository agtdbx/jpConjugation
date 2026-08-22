from parsing.load import load_json_file
from parsing.verbe import parse_conjugation_data
from verbes.present import  get_godan_present_formes, \
                            get_ichidan_present_formes, \
                            get_exception_present_formes
from verbes.passe import    get_godan_passe_formes, \
                            get_ichidan_passe_formes, \
                            get_exception_passe_formes

if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/data.json")

    print("------------------------------------------------------------------------------------")
    for verbe_data in json_data["verbes"]:

        verbe_parse = parse_conjugation_data(verbe_data)

        verbe = verbe_parse['verbe']
        terminaison = verbe_parse['terminaison']
        radical = verbe_parse['radical']

        for temps_id in ["pr", "pa"]:
            temps = ""
            forme_ip = ""
            forme_fp = ""
            forme_in = ""
            forme_fn = ""

            ###########################################################################################
            # Présent
            ###########################################################################################
            if temps_id == "pr":
                temps = "Présent"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_godan_present_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_ichidan_present_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_exception_present_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ###########################################################################################
            # Passé
            ###########################################################################################
            if temps_id == "pa":
                temps = "Passé"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_godan_passe_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_ichidan_passe_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_exception_passe_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            print(f"| {temps:8} | {forme_ip:10} | {forme_fp:15} | {forme_in:15} | {forme_fn:20} |")

        print("------------------------------------------------------------------------------------")