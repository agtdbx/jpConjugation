DATA_FILE_PATH = "./data/data.json"

VERBS_TYPES = {
    "godan" : "Godan",
    "ichidan" : "Ichidan",
    "exception" : "Exception"
}

VERBS_TENSES = {
    "pr" :     "Présent",            # Present
    "pa" :     "Passé",              # Past
    "im-te" :  "Impératif -te",      # Imperative -te
    "im-ro" :  "Impératif -ro",      # Imperative -ro
    "pro" :    "Progressif",         # Progressive
    "de-pr" :  "Volonté présent",    # Desirative present
    "de-pa" :  "Volonté passé",      # Desirative past
    "vo" :     "Invitation",         # Volitional
    "po-pr" :  "Potentiel présent",  # Potential present
    "po-pa" :  "Potentiel passé",    # Potential past
    "co-ba" :  "Conditionnel -ba",   # Conditional -ba
    "co-ta" :  "Conditionnel -tara", # Conditional -tara

    # "pas" :    "Passif",             # Passive
    # "ca" :     "Causatif",           # Causative
    # "ca-pas" : "Causatif passif",    # Causative passive
}

VERBS_ALLOWED_FORMS = {
    "pr" :     ["ip", "fp", "in", "fn"],
    "pa" :     ["ip", "fp", "in", "fn"],
    "im-te" :  ["ip", "fp", "in", "fn"],
    "im-ro" :  ["ip", "in"],
    "pro" :    ["ip", "fp", "in", "fn"],
    "de-pr" :  ["ip", "fp", "in", "fn"],
    "de-pa" :  ["ip", "fp", "in", "fn"],
    "vo" :     ["ip", "fp"],
    "po-pr" :  ["ip", "fp", "in", "fn"],
    "po-pa" :  ["ip", "fp", "in", "fn"],
    "co-ba" :  ["ip", "in"],
    "co-ta" :  ["ip"],

    # "pas" :    ["ip", "fp", "in", "fn"],
    # "ca" :     ["ip", "fp", "in", "fn"],
    # "ca-pas" : ["ip", "fp", "in", "fn"],
}

VERBS_ENDINGS = ["tsu", "ru", "mu", "nu", "bu", "ku", "gu", "su", "u"]


ADJECTIVES_TYPES = {
    "i" : "i",
    "na" : "na"
}

ADJECTIVES_TENSES = {
    "pr" : "Présent",   # Present
    "pa" : "Passé",     # Past
    "co" : "Liaison",   # Connective
    "ad" : "Adverbiale" # Adverbial
}

ADJECTIVES_ALLOWED_FORMS = {
    "pr" : ["ip", "fp", "in", "fn"],
    "pa" : ["ip", "fp", "in", "fn"],
    "co" : ["ip", "in"],
    "ad" : ["ip"],
}

ADJECTIVES_EXCEPTIONS = {
    "ii" : "yo",
    "kakkoii" : "kakkoyo",
}


FORMS = {
    "ip" : "Informel Positif",
    "fp" : "Formel Positif",
    "in" : "Informel Négatif",
    "fn" : "Formel Négatif"
}
