from jpconjugation.models import Adjective
from jpconjugation.conjugation.adjectives.present import get_present_forms, get_present_rules
from jpconjugation.conjugation.adjectives.past import get_past_forms, get_past_rules
from jpconjugation.conjugation.adjectives.connective import get_connective_forms, get_connective_rules
from jpconjugation.conjugation.adjectives.adverbial import get_adverbial_forms, get_adverbial_rules

_ADJECTIVE_TENSES_FUNCTIONS = {
    "pr" : get_present_forms,
    "pa" : get_past_forms,
    "co" : get_connective_forms,
    "ad" : get_adverbial_forms,
}

_ADJECTIVE_TENSES_RULES = {
    "pr" : get_present_rules,
    "pa" : get_past_rules,
    "co" : get_connective_rules,
    "ad" : get_adverbial_rules,
}


def conjugate_adjective(adjective: Adjective, tense_id: str) -> dict:
    fnct = _ADJECTIVE_TENSES_FUNCTIONS.get(tense_id)

    if fnct != None:
        return fnct(adjective)

    return {}


def get_adjective_rules(adjective: Adjective, tense_id: str) -> dict:
    fnct = _ADJECTIVE_TENSES_RULES.get(tense_id)

    if fnct != None:
        return fnct(adjective)

    return {}