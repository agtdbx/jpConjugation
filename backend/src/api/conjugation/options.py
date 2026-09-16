from jpconjugation.define import (
    VERBS_TYPES, VERBS_TENSES,
    VERBS_CONJUGATION_ORDER,
    ADJECTIVES_TYPES, ADJECTIVES_TENSES,
    ADJECTIVES_CONJUGATION_ORDER,
    FORMS
)

def get_conjugation_options() -> dict:
    return {
        "forms": {
            "title": "Formes finales (Politesse & Polarité)",
            "values": FORMS
        },
        "categories": {
            "verbs": {
                "title": "Verbes",
                "types": VERBS_TYPES,
                "values": VERBS_TENSES,
                "orders": VERBS_CONJUGATION_ORDER,
            },
            "adjectives": {
                "title": "Adjectifs",
                "types": ADJECTIVES_TYPES,
                "values": ADJECTIVES_TENSES,
                "orders": ADJECTIVES_CONJUGATION_ORDER,
            }
        }
    }
