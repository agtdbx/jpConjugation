from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.present import get_present_forms
from jpconjugation.conjugation.verbs.past import get_past_forms
from jpconjugation.conjugation.verbs.imperative import get_imperative_forms
from jpconjugation.conjugation.verbs.progressive import get_progressive_forms
from jpconjugation.conjugation.verbs.desirative import get_desirative_present_forms, get_desirative_past_forms
from jpconjugation.conjugation.verbs.volitional import get_volitional_forms
from jpconjugation.conjugation.verbs.potential import get_potential_forms

_VERB_TENSES_FUNCTIONS = {
    "pr" : get_present_forms,
    "pa" : get_past_forms,
    "im" : get_imperative_forms,
    "pro" : get_progressive_forms,
    "de-pr" : get_desirative_present_forms,
    "de-pa" : get_desirative_past_forms,
    "vo" : get_volitional_forms,
    "po" : get_potential_forms,
}


def conjugate_verb(verb: Verb, tense_id: str) -> dict:
    fnct = _VERB_TENSES_FUNCTIONS.get(tense_id)

    if fnct != None:
        return fnct(verb)

    return {}
