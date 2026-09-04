from jpconjugation.define import VERBS_TENSES
from jpconjugation.parsing.load import load_json_file
from jpconjugation.conjugation.verbs.conjugation import conjugate_verb

if __name__ == "__main__":
    # Get and parse json data
    try:
        data = load_json_file("./data/data.json")
    except Exception as e:
        print(f"Error : {e}")

    separator = "-" * 111

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":20} |")
    print(separator)

    for verb in data.verbs:

        for tense_id, tense_name in VERBS_TENSES.items():
            forms = conjugate_verb(verb, tense_id)
            form_ip = forms.get("ip", "")
            form_fp = forms.get("fp", "")
            form_in = forms.get("in", "")
            form_fn = forms.get("fn", "")

            print(f"| {tense_name:15} | {form_ip:20} | {form_fp:20} | {form_in:20} | {form_fn:20} |")

        print(separator)