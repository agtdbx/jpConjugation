from jpconjugation.models import Verb
from jpconjugation.conjugation.verbs.present import get_present_forms, get_present_rules
from jpconjugation.conjugation.verbs.past import get_past_forms, get_past_rules
from jpconjugation.conjugation.verbs.imperative import (
    get_imperative_te_forms, get_imperative_te_rules,
    get_imperative_ro_forms, get_imperative_ro_rules
)
from jpconjugation.conjugation.verbs.progressive import get_progressive_forms, get_progressive_rules
from jpconjugation.conjugation.verbs.desirative import (
    get_desirative_present_forms, get_desirative_present_rules,
    get_desirative_past_forms, get_desirative_past_rules
)
from jpconjugation.conjugation.verbs.volitional import get_volitional_forms, get_volitional_rules
from jpconjugation.conjugation.verbs.potential import (
    get_potential_present_forms, get_potential_present_rules,
    get_potential_past_forms, get_potential_past_rules,
)
from jpconjugation.conjugation.verbs.conditional import (
    get_conditional_ba_forms, get_conditional_ba_rules,
    get_conditional_tara_forms, get_conditional_tara_rules,
)
from jpconjugation.conjugation.verbs.passive import get_passive_forms, get_passive_rules
from jpconjugation.conjugation.verbs.causative import (
    get_causative_forms, get_causative_rules,
    get_causative_passive_forms, get_causative_passive_rules,
)

_VERB_TENSES_FUNCTIONS = {
    "pr" : get_present_forms,
    "pa" : get_past_forms,
    "im-te" : get_imperative_te_forms,
    "im-ro" : get_imperative_ro_forms,
    "pro" : get_progressive_forms,
    "de-pr" : get_desirative_present_forms,
    "de-pa" : get_desirative_past_forms,
    "vo" : get_volitional_forms,
    "po-pr" : get_potential_present_forms,
    "po-pa" : get_potential_past_forms,
    "co-ba" : get_conditional_ba_forms,
    "co-ta" : get_conditional_tara_forms,
    "pas" : get_passive_forms,
    "ca" : get_causative_forms,
    "ca-pas" : get_causative_passive_forms,
}

_VERB_TENSES_RULES = {
    "pr" : get_present_rules,
    "pa" : get_past_rules,
    "im-te" : get_imperative_te_rules,
    "im-ro" : get_imperative_ro_rules,
    "pro" : get_progressive_rules,
    "de-pr" : get_desirative_present_rules,
    "de-pa" : get_desirative_past_rules,
    "vo" : get_volitional_rules,
    "po-pr" : get_potential_present_rules,
    "po-pa" : get_potential_past_rules,
    "co-ba" : get_conditional_ba_rules,
    "co-ta" : get_conditional_tara_rules,
    "pas" : get_passive_rules,
    "ca" : get_causative_rules,
    "ca-pas" : get_causative_passive_rules,
}


def conjugate_verb(verb: Verb, tense_id: str) -> dict:
    fnct = _VERB_TENSES_FUNCTIONS.get(tense_id)

    if fnct != None:
        return fnct(verb)

    return {}


def get_verb_rules(verb: Verb, tense_id: str) -> dict:
    fnct = _VERB_TENSES_RULES.get(tense_id)

    if fnct != None:
        return fnct(verb)

    return {}
