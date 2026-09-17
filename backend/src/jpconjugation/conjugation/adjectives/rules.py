from jpconjugation.define import ADJECTIVES_EXCEPTIONS
from jpconjugation.models import Adjective

# SUFFIXES_PRESENT = {"ip": "ru", "fp": "masu", "in": "nai", "fn": "masen"}
# SUFFIXES_PAST = {"ip": "ta", "fp": "mashita", "in": "nakatta", "fn": "masen deshita"}

def build_core_rules(
        adjective: Adjective,
        i_rules: dict,
        na_rules: dict,
    ) -> dict:
    if adjective.type == "i":
        exception = ""
        if adjective.romaji in ADJECTIVES_EXCEPTIONS:
            exception = f"Radical : '{adjective.stem}'. "
        return {
            form: f"{exception}Pour un i adjectif, {i_rules.get(form, "règle manquante")}."
            for form in i_rules.keys()
        }
    elif adjective.type == "na":
        return {
            form: f"Pour un na adjectif, {na_rules.get(form, "règle manquante")}."
            for form in na_rules.keys()
        }
    return {}


# def build_derived_rules(
#         adjective: Adjective,
#         godan_action: str,
#         ichidan_action: str,
#         base_suffixes: dict,
#         godan_prefix: str = "",
#         ichidan_prefix: str = "",
#         exception_rules: dict = {}
#     ) -> dict:
#     if adjective.type == "godan":
#         return {
#             form: f"Pour un adjectif Godan, {godan_action} et ajoute '{godan_prefix}{suffix}'."
#             for form, suffix in base_suffixes.items()
#         }

#     elif adjective.type == "ichidan":
#         return {
#             form: f"Pour un adjectif Ichidan, {ichidan_action} et ajoute '{ichidan_prefix}{suffix}'."
#             for form, suffix in base_suffixes.items()
#         }

#     elif adjective.type == "exception":
#         return {
#             form: f"Exception ({adjective.romaji}) : {exception_rules.get(form, "La forme est irrégulière")}."
#             for form in base_suffixes.keys()
#         }

#     return {}
