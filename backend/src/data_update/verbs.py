from jpconjugation.define import VERBS_TYPES
from jpconjugation.models import Verb
from data_update.parsing import get_word_parts_from_card
from data_update.jisho_api import get_verb_type_from_jisho

def get_verb_if_needed(
        current_verbs: set[str],
        recto: str,
        verso: str
        ) -> Verb | None:
    parts = get_word_parts_from_card(recto, verso)
    if not parts:
        return None
    kanji, romaji, traduction = parts

    if kanji in current_verbs:
        return None

    type = get_verb_type_from_jisho(recto)
    if type not in VERBS_TYPES.keys():
        return None

    return Verb(
        kanji=kanji,
        romaji=romaji,
        type=type,
        traduction=traduction)
