from parsing.load import load_json_file
from parsing.adjectives import parse_conjugation_data
from adjectives.present import get_present_forms
from adjectives.past import get_past_forms
from adjectives.connective import get_connective_forms
from adjectives.adverbiale import get_adverbiale_forms


if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/test.json")

    separator = "-" * 121

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":30} |")
    print(separator)
    for adjectif_data in json_data["adjectives"]:

        adjectif_parse = parse_conjugation_data(adjectif_data)

        for form_id in ["pr", "pa", "co", "ad"]:
            form = ""
            form_ip = ""
            form_fp = ""
            form_in = ""
            form_fn = ""

            ##############################################################
            # Present
            ##############################################################
            if form_id == "pr":
                form = "Présent"
                formes = get_present_forms(adjectif_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Past
            ##############################################################
            elif form_id == "pa":
                form = "Passé"
                formes = get_past_forms(adjectif_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Connective
            ##############################################################
            elif form_id == "co":
                form = "Liaison"
                formes = get_connective_forms(adjectif_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Adverbiale
            ##############################################################
            elif form_id == "ad":
                form = "Adverbale"
                formes = get_adverbiale_forms(adjectif_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            print(f"| {form:15} | {form_ip:20} | {form_fp:20} | {form_in:20} | {form_fn:30} |")

        print(separator)