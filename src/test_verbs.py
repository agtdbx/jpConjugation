from parsing.load import load_json_file
from parsing.verbs import parse_conjugation_data
from verbs.present import get_present_forms
from verbs.past import get_past_forms
from verbs.imperative import get_imperative_forms
from verbs.progressive import get_progressive_forms
from verbs.desirative import get_desirative_present_forms, get_desirative_past_forms
from verbs.volitional import get_volitional_forms
from verbs.potential import get_potential_forms


if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/test.json")

    separator = "-" * 111

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":20} |")
    print(separator)
    for verbe_data in json_data["verbs"]:

        verbe_parse = parse_conjugation_data(verbe_data)

        for form_id in ["pr", "pa", "im", "pro", "de-pr", "de-pa", "vo", "po"]:
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
                formes = get_present_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Past
            ##############################################################
            elif form_id == "pa":
                form = "Passé"
                formes = get_past_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Imperative
            ##############################################################
            elif form_id == "im":
                form = "Impératif"
                formes = get_imperative_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Progressive
            ##############################################################
            elif form_id == "pro":
                form = "Progressive"
                formes = get_progressive_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Desirative present
            ##############################################################
            elif form_id == "de-pr":
                form = "Volonté présent"
                formes = get_desirative_present_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Desirative past
            ##############################################################
            elif form_id == "de-pa":
                form = "Volonté passé"
                formes = get_desirative_past_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Volitional
            ##############################################################
            elif form_id == "vo":
                form = "Invitation"
                formes = get_volitional_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            ##############################################################
            # Potential
            ##############################################################
            elif form_id == "po":
                form = "Potentielle"
                formes = get_potential_forms(verbe_parse)
                form_ip = formes.get("ip", "")
                form_fp = formes.get("fp", "")
                form_in = formes.get("in", "")
                form_fn = formes.get("fn", "")

            print(f"| {form:15} | {form_ip:20} | {form_fp:20} | {form_in:20} | {form_fn:20} |")

        print(separator)