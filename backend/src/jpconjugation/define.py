###########################################################################################
# VERBS
###########################################################################################

VERBS_TYPES = {
    "godan" : "Godan",
    "ichidan" : "Ichidan",
    "exception" : "Exception"
}

VERBS_TENSES = {
    # Root
    "pr" :    "Présent",            # Present
    "pa" :    "Passé",              # Past
    "im-te" : "Impératif -te",      # Imperative -te
    "im-ro" : "Impératif -ro",      # Imperative -ro
    "vo" :    "Invitation",         # Volitional
    "co-ba" : "Conditionnel -ba",   # Conditional -ba
    "co-ta" : "Conditionnel -tara", # Conditional -tara

    # Derivative
    "de" :    "Désiratif",          # Desirative
    "pro" :   "Progressif",         # Progressive
    "po" :    "Potentiel",          # Potential
    "pas" :   "Passif",             # Passive
    "ca" :    "Causatif",           # Causative
}

VERBS_ALLOWED_FORMS = {
    # Root
    "pr" :     ["ip", "fp", "in", "fn"],
    "pa" :     ["ip", "fp", "in", "fn"],
    "im-te" :  ["ip", "fp", "in", "fn"],
    "im-ro" :  ["ip", "in"],
    "vo" :     ["ip", "fp"],
    "co-ba" :  ["ip", "in"],
    "co-ta" :  ["ip"],

    # Derivative
    "de" :     ["ip"],
    "pro" :    ["ip"],
    "po" :     ["ip"],
    "pas" :    ["ip"],
    "ca" :     ["ip"],
}

VERBS_CONJUGATION_ORDER = {
    # Root
    "pr" :    0,
    "pa" :    0,
    "im-te" : 0,
    "im-ro" : 0,
    "vo" :    0,
    "co-ba" : 0,
    "co-ta" : 0,

    # Derivative
    "de" :    1,
    "pro" :   2,
    "po" :    2,
    "pas" :   3,
    "ca" :    4,
}

VERBS_TO_ADJECTIVES_TENSE = [
    "de"
]

VERBS_ENDINGS = ["tsu", "ru", "mu", "nu", "bu", "ku", "gu", "su", "u"]

###########################################################################################
# ADJECTIVES
###########################################################################################

ADJECTIVES_TYPES = {
    "i" : "i",
    "na" : "na"
}

ADJECTIVES_TENSES = {
    # Root
    "pr"    : "Présent",            # Present
    "pa"    : "Passé",              # Past
    "co"    : "Liaison",            # Connective
    "ad"    : "Adverbiale",         # Adverbial
    "co-ba" : "Conditionnel -ba",   # Conditional -ba
    "co-ta" : "Conditionnel -tara", # Conditional -tara

    # # Derivative
    # "con"   : "Conjecture",         # Conjecture
    # "ex"    : "Excès",              # Excess
}

ADJECTIVES_ALLOWED_FORMS = {
    # Root
    "pr"    : ["ip", "fp", "in", "fn"],
    "pa"    : ["ip", "fp", "in", "fn"],
    "co"    : ["ip", "in"],
    "ad"    : ["ip"],
    "co-ba" : ["ip", "in"],
    "co-ta" : ["ip", "in"],

    # # Derivative
    # "con"   : ["ip"],
    # "ex"    : ["ip"],
}

ADJECTIVES_CONJUGATION_ORDER = {
    # Root
    "pr"    : 0,
    "pa"    : 0,
    "co"    : 0,
    "ad"    : 0,
    "co-ba" : 0,
    "co-ta" : 0,

    # # Derivative
    # "con"   : 1,
    # "ex"    : 1,
}

ADJECTIVES_TO_VERBS_TENSE = [
    "ex"
]

ADJECTIVES_EXCEPTIONS = {
    "ii" : "yo",
    "kakkoii" : "kakkoyo",
}

###########################################################################################
# OTHERS
###########################################################################################

DATA_FILE_PATH = "./data/data.json"

FORMS = {
    "ip" : "Informel Positif",
    "fp" : "Formel Positif",
    "in" : "Informel Négatif",
    "fn" : "Formel Négatif"
}
