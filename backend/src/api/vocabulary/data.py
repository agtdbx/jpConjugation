import re
import jaconv
from jpconjugation.define import (
    VERBS_TENSES, VERBS_ALLOWED_FORMS, VERBS_CONJUGATION_ORDER,
    ADJECTIVES_TENSES, ADJECTIVES_ALLOWED_FORMS, ADJECTIVES_CONJUGATION_ORDER,
    FORMS
)
from jpconjugation.vocabulary.tenses import (
    VERBS_TENSES_DEFINITION,
    ADJECTIVES_TENSES_DEFINITION
)
from jpconjugation.models import JPData, Verb, Adjective
from jpconjugation.conjugation.verbs.conjugation import get_verb_rules
from jpconjugation.conjugation.adjectives.conjugation import get_adjective_rules

def get_vocabulary_data(data: JPData) -> dict:
    return {
        "forms" : FORMS,
        "verbs" : _get_words(data.verbs),
        "adjectives" : _get_words(data.adjectives),
        "tenses" : {
            "verbs" : _get_tenses(
                VERBS_TENSES,
                VERBS_ALLOWED_FORMS,
                VERBS_CONJUGATION_ORDER,
                VERBS_TENSES_DEFINITION,
                verb=True),
            "adjectives" : _get_tenses(
                ADJECTIVES_TENSES,
                ADJECTIVES_ALLOWED_FORMS,
                ADJECTIVES_CONJUGATION_ORDER,
                ADJECTIVES_TENSES_DEFINITION,
                verb=False),
        },
    }


def _get_words(
        words: list
        ) -> list[dict]:
    words_info = []

    for word in words:
        words_info.append({
            "romaji" : word.romaji,
            "kana" : _word_to_kana(word),
            "kanji" : word.kanji,
            "traduction" : word.traduction,
            "type" : word.type,
        })

    return words_info


def _word_to_kana(word: Verb | Adjective) -> str:
    if bool(re.search(r'[\u4E00-\u9FFF]', word.romaji)):
        return jaconv.alphabet2kana(word.romaji)
    return word.kanji


def _get_tenses(
        tenses: dict,
        allowed_forms: dict,
        conjugation_orders: dict,
        info: dict,
        verb: bool
        ) -> list[dict]:
    verb_godan = Verb(romaji="iku", kanji="行く", traduction="aller", type="godan", stem="ik", ending="u")
    verb_ichidan = Verb(romaji="taberu", kanji="食べる", traduction="manger", type="ichidan", stem="tabe", ending="ru")
    verb_exception_suru = Verb(romaji="suru", kanji="する", traduction="faire", type="exception", stem="su", ending="ru")
    adjective_i = Adjective(romaji="furui", kanji="古い", traduction="vieux", type="i", stem="furu")
    adjective_na = Adjective(romaji="kirei", kanji="綺麗", traduction="joli", type="na", stem="kirei")

    tense_type = "verbs" if verb else "adjectives"

    tenses_info = []
    for tense_id, tense_name in tenses.items():
        if verb:
            rules = {
                "godan": get_verb_rules(verb_godan, tense_id),
                "ichidan": get_verb_rules(verb_ichidan, tense_id),
                "exception": get_verb_rules(verb_exception_suru, tense_id),
            }
        else:
            rules = {
                "i": get_adjective_rules(adjective_i, tense_id),
                "na": get_adjective_rules(adjective_na, tense_id),
            }

        tenses_info.append({
            "name": tense_name,
            "allowedForms": allowed_forms.get(tense_id, []),
            "order": conjugation_orders.get(tense_id, -1),
            "info": info.get(tense_id, "Pas de description."),
            "rules": rules,
            "type": tense_type,
        })

    return tenses_info
