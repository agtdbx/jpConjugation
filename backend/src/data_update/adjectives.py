from jpconjugation.define import ADJECTIVES_TYPES
from jpconjugation.models import Adjective
from data_update.parsing import get_word_parts_from_card
from data_update.jisho_api import get_adjective_type_from_jisho

def get_adjective_if_needed(
        current_adjectives: set[str],
        recto: str,
        verso: str
        ) -> Adjective | None:
    parts = get_word_parts_from_card(recto, verso)
    if not parts:
        return None
    kanji, romaji, traduction = parts

    if kanji in current_adjectives:
        return None

    type = get_adjective_type_from_jisho(recto)
    if type not in ADJECTIVES_TYPES.keys():
        return None

    return Adjective(
        kanji=kanji,
        romaji=romaji,
        type=type,
        traduction=traduction)
