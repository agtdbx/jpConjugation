from jpconjugation.define import ADJECTIVES_EXCEPTIONS
from jpconjugation.models import Adjective

def build_rules(
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
