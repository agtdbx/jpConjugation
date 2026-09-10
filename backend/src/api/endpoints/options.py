from jpconjugation.define import (
    VERBS_TYPES, VERBS_TENSES,
    ADJECTIVES_TYPES, ADJECTIVES_TENSES,
    FORMS
)

def get_conjugation_options() -> dict:
    return {
        "sections": {
            "forms": {
                "title": "Formes",
                "types": {},
                "values": FORMS
            },
            "verbs": {
                "title": "Verbes",
                "types": VERBS_TYPES,
                "values": VERBS_TENSES
            },
            "adjectives": {
                "title": "Adjectifs",
                "types": ADJECTIVES_TYPES,
                "values": ADJECTIVES_TENSES
            }
        }
    }
