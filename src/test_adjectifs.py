from parsing.load import load_json_file
from parsing.adjectif import parse_conjugation_data
from adjectifs.present import get_present_i_formes, get_present_na_formes
from adjectifs.passee import get_passee_i_formes, get_passee_na_formes
from adjectifs.liaison import get_liaison_i_formes, get_liaison_na_formes
from adjectifs.adverbale import get_adverbale_i_formes, get_adverbale_na_formes


if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/test.json")

    separator = "-" * 121

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":30} |")
    print(separator)
    for adjectif_data in json_data["adjectifs"]:

        adjectif_parse = parse_conjugation_data(adjectif_data)

        for temps_id in ["pr", "pa", "li", "ad"]:
            temps = ""
            forme_ip = ""
            forme_fp = ""
            forme_in = ""
            forme_fn = ""

            ##############################################################
            # Présent
            ##############################################################
            if temps_id == "pr":
                temps = "Présent"
                formes = {}
                if adjectif_parse["type"] == "i":
                    formes = get_present_i_formes(adjectif_parse)
                elif adjectif_parse["type"] == "na":
                    formes = get_present_na_formes(adjectif_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Passé
            ##############################################################
            elif temps_id == "pa":
                temps = "Passé"
                formes = {}
                if adjectif_parse["type"] == "i":
                    formes = get_passee_i_formes(adjectif_parse)
                elif adjectif_parse["type"] == "na":
                    formes = get_passee_na_formes(adjectif_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Liason
            ##############################################################
            elif temps_id == "li":
                temps = "Liason"
                formes = {}
                if adjectif_parse["type"] == "i":
                    formes = get_liaison_i_formes(adjectif_parse)
                elif adjectif_parse["type"] == "na":
                    formes = get_liaison_na_formes(adjectif_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Adverbale
            ##############################################################
            elif temps_id == "ad":
                temps = "Adverbale"
                formes = {}
                if adjectif_parse["type"] == "i":
                    formes = get_adverbale_i_formes(adjectif_parse)
                elif adjectif_parse["type"] == "na":
                    formes = get_adverbale_na_formes(adjectif_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            print(f"| {temps:15} | {forme_ip:20} | {forme_fp:20} | {forme_in:20} | {forme_fn:30} |")

        print(separator)