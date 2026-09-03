from jpconjugation.define import VERB_FORMS, VERB_FORMS_NAME
from jpconjugation.parsing.load import load_json_file
from jpconjugation.parsing.verbs import parse_conjugation_data
from jpconjugation.conjugation.verbs.conjugation import conjugate_verb

if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/test.json")

    separator = "-" * 111

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":20} |")
    print(separator)
    for verb_data in json_data["verbs"]:

        verb_parse = parse_conjugation_data(verb_data)

        for form_id in VERB_FORMS:
            form_name = VERB_FORMS_NAME.get(form_id, "")
            forms = conjugate_verb(verb_parse, form_id)
            form_ip = forms.get("ip", "")
            form_fp = forms.get("fp", "")
            form_in = forms.get("in", "")
            form_fn = forms.get("fn", "")

            print(f"| {form_name:15} | {form_ip:20} | {form_fp:20} | {form_in:20} | {form_fn:20} |")

        print(separator)