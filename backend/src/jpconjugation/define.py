DATA_FILE_PATH = "./data/data.json"

VERBS_TYPES = {
    "godan" : "Godan",
    "ichidan" : "Ichidan",
    "exception" : "Exception"
}

VERBS_TENSES = {
    "pr" : "Présent",            # Present
    "pa" : "Passé",              # Past
    "im-so" : "Impératif doux",  # Imperative soft
    "im-ha" : "Impératif dur",   # Imperative hard
    "pro" : "Progressif",        # Progressive
    "de-pr" : "Volonté présent", # Desirative present
    "de-pa" : "Volonté passé",   # Desirative past
    "vo" : "Invitation",         # Volitional
    "po" : "Potentielle"         # Potential
}

VERBS_ALLOWED_FORMS = {
    "pr" : ["ip", "fp", "in", "fn"],
    "pa" : ["ip", "fp", "in", "fn"],
    "im-so" : ["ip", "fp", "in", "fn"],
    "im-ha" : ["ip", "in"],
    "pro" : ["ip", "fp", "in", "fn"],
    "de-pr" : ["ip", "fp", "in", "fn"],
    "de-pa" : ["ip", "fp", "in", "fn"],
    "vo" : ["ip", "fp"],
    "po" : ["ip", "fp", "in", "fn"],
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
