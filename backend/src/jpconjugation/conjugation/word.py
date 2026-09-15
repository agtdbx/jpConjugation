from jpconjugation.define import (
    VERBS_CONJUGATION_ORDER,
    VERBS_TO_ADJECTIVES_TENSE,
    ADJECTIVES_CONJUGATION_ORDER,
)
from jpconjugation.models import Verb, Adjective
from jpconjugation.conjugation.verbs.conjugation import conjugate_verb, get_verb_rules
from jpconjugation.conjugation.adjectives.conjugation import conjugate_adjective, get_adjective_rules

def conjugate_word(
        word: Verb | Adjective,
        tense_chain: str
        ) -> dict:
    tenses = tense_chain.split('|')
    if not _is_conjugation_possible(word, tenses):
        return {}

    # Conjugate word with derivated tenses
    current_word = word
    for tense in tenses[:-1]:
        if isinstance(current_word, Verb):
            tmp_dict = conjugate_verb(current_word, tense)
        else:
            tmp_dict = conjugate_adjective(current_word, tense)

        if not "ip" in tmp_dict.keys():
            return {}

        if isinstance(current_word, Verb) and tense not in VERBS_TO_ADJECTIVES_TENSE:
            current_word = Verb(
                romaji=tmp_dict["ip"],
                kanji=current_word.kanji,
                traduction=current_word.traduction,
                type="ichidan",
                stem=tmp_dict["ip"][:-2],
                ending="ru"
            )
        else:
            current_word = Adjective(
                romaji=tmp_dict["ip"],
                kanji=current_word.kanji,
                traduction=current_word.traduction,
                type="i",
                stem=tmp_dict["ip"][:-1],
            )

    # Conjugate word with root tenses
    if isinstance(current_word, Verb):
        return conjugate_verb(current_word, tenses[-1])
    else:
        return conjugate_adjective(current_word, tenses[-1])


def get_word_rules(
        word: Verb | Adjective,
        tense_chain: str
        ) -> dict:
    tenses = tense_chain.split('|')
    if not _is_conjugation_possible(word, tenses):
        return {}

    # Get word rules for last tenses
    current_word = word
    if isinstance(current_word, Verb):
        return get_verb_rules(current_word, tenses[-1])
    else:
        return get_adjective_rules(current_word, tenses[-1])


def _is_conjugation_possible(
        word: Verb | Adjective,
        tenses: list[str]
        ) -> bool:
    # Get word type
    if isinstance(word, Verb):
        word_type = "verb"
    else:
        word_type = "adjective"

    # Check tenses combinaisons
    tense_order_id = 10
    for tense in tenses:
        if word_type == "verb":
            tense_order = VERBS_CONJUGATION_ORDER.get(tense)
            if tense in VERBS_TO_ADJECTIVES_TENSE:
                word_type = "adjective"
        else:
            tense_order = ADJECTIVES_CONJUGATION_ORDER.get(tense)

        if tense_order == None:
            return False

        if tense_order >= tense_order_id:
            return False
        tense_order_id = tense_order

    return True
