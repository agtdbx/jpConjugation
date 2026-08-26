from jpconjugation.define import ADJECTIVES_FORMS, AJDJECTIVES_FORMS_NAME
from jpconjugation.parsing.load import load_json_file
from jpconjugation.parsing.adjectives import parse_conjugation_data
from jpconjugation.conjugation.adjectives.conjugation import conjugate_adjective


if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/test.json")

    separator = "-" * 121

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":30} |")
    print(separator)
    for adjective_data in json_data["adjectives"]:

        adjective_parse = parse_conjugation_data(adjective_data)

        for form_id in ADJECTIVES_FORMS:
            form_name = AJDJECTIVES_FORMS_NAME.get(form_id, "")
            forms = conjugate_adjective(adjective_parse, form_id)
            form_ip = forms.get("ip", "")
            form_fp = forms.get("fp", "")
            form_in = forms.get("in", "")
            form_fn = forms.get("fn", "")

            print(f"| {form_name:15} | {form_ip:20} | {form_fp:20} | {form_in:20} | {form_fn:30} |")

        print(separator)