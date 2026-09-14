from jpconjugation.models import Verb

SUFFIXES_PRESENT = {"ip": "ru", "fp": "masu", "in": "nai", "fn": "masen"}
SUFFIXES_PAST = {"ip": "ta", "fp": "mashita", "in": "nakatta", "fn": "masen deshita"}

def build_core_rules(
    verb: Verb,
    godan_rules: dict,
    ichidan_rules: dict,
    exception_rules: dict = {}
) -> dict:
    if verb.type == "godan":
        return {
            form: f"Pour un verbe Godan, {godan_rules.get(form, "règle manquante")}."
            for form in godan_rules.keys()
        }
    elif verb.type == "ichidan":
        return {
            form: f"Pour un verbe Ichidan, {ichidan_rules.get(form, "règle manquante")}."
            for form in ichidan_rules.keys()
        }
    elif verb.type == "exception":
        return {
            form: f"Exception ({verb.romaji}) : {exception_rules.get(form, "La forme est irrégulière")}."
            for form in godan_rules.keys()
        }
    return {}


def build_derived_rules(
        verb: Verb,
        godan_action: str,
        ichidan_action: str,
        base_suffixes: dict,
        godan_prefix: str = "",
        ichidan_prefix: str = "",
        exception_rules: dict = {}
    ) -> dict:
    if verb.type == "godan":
        return {
            form: f"Pour un verbe Godan, on {godan_action} et on ajoute '{godan_prefix}{suffix}'."
            for form, suffix in base_suffixes.items()
        }

    elif verb.type == "ichidan":
        return {
            form: f"Pour un verbe Ichidan, on {ichidan_action} et on ajoute '{ichidan_prefix}{suffix}'."
            for form, suffix in base_suffixes.items()
        }

    elif verb.type == "exception":
        return {
            form: f"Exception ({verb.romaji}) : {exception_rules.get(form, "La forme est irrégulière")}."
            for form in base_suffixes.keys()
        }

    return {}
