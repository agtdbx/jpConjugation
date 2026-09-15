from jpconjugation.define import (
    VERBS_CONJUGATION_ORDER,
    VERBS_TO_ADJECTIVES_TENSE,
    ADJECTIVES_CONJUGATION_ORDER,
)
from jpconjugation.models import Verb, Adjective
from jpconjugation.conjugation.verbs.conjugation import conjugate_verb
from jpconjugation.conjugation.adjectives.conjugation import conjugate_adjective

def conjugate_word(
        word: Verb | Adjective,
        tense_chain: str
        ) -> dict:
    tenses = tense_chain.split('|')
    current_word = word

    # Get word type
    if isinstance(current_word, Verb):
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
            return {}

        if tense_order >= tense_order_id:
            return {}
        tense_order_id = tense_order

    # Conjugate word with derivated tenses
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
