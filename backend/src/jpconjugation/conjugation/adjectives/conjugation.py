from jpconjugation.conjugation.adjectives.present import get_present_forms
from jpconjugation.conjugation.adjectives.past import get_past_forms
from jpconjugation.conjugation.adjectives.connective import get_connective_forms
from conjugation.adjectives.adverbial import get_adverbial_forms

_ADJECTIVE_TENSES_FUNCTIONS = {
    "pr" : get_present_forms,
    "pa" : get_past_forms,
    "co" : get_connective_forms,
    "ad" : get_adverbial_forms,
}


def conjugate_adjective(adjective: Adjective, form_id: str) -> dict:
    fnct = _ADJECTIVE_TENSES_FUNCTIONS.get(form_id)

    if fnct != None:
        return fnct(adjective)

    return {}