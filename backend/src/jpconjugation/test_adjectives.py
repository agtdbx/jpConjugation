from jpconjugation.define import ADJECTIVES_TENSES, AJDJECTIVES_TENSES_NAME
from jpconjugation.parsing.load import load_json_file
from jpconjugation.conjugation.adjectives.conjugation import conjugate_adjective


if __name__ == "__main__":
    # Get and parse json data
    try:
        data = load_json_file("./data/data.json")
    except Exception as e:
        print(f"Error : {e}")

    separator = "-" * 121

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":30} |")
    print(separator)
    for adjective in data.adjectives:
        for form_id in ADJECTIVES_TENSES:
            form_name = AJDJECTIVES_TENSES_NAME.get(form_id, "")
            forms = conjugate_adjective(adjective, form_id)
            form_ip = forms.get("ip", "")
            form_fp = forms.get("fp", "")
            form_in = forms.get("in", "")
            form_fn = forms.get("fn", "")

            print(f"| {form_name:15} | {form_ip:20} | {form_fp:20} | {form_in:20} | {form_fn:30} |")

        print(separator)