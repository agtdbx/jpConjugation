from jpconjugation.models import Verb

def get_base_a(verb: Verb) -> str:
    return BASE_A[verb.ending]

def get_base_e(verb: Verb) -> str:
    return BASE_E[verb.ending]

def get_base_i(verb: Verb) -> str:
    return BASE_I[verb.ending]

def get_base_o(verb: Verb) -> str:
    return BASE_O[verb.ending]

def get_base_ta(verb: Verb) -> str:
    return BASE_TA[verb.ending]

def get_base_te(verb: Verb) -> str:
    return BASE_TE[verb.ending]

BASE_A = {
    "u" : "wa",
    "tsu" : "ta",
    "ru" : "ra",
    "mu" : "ma",
    "nu" : "na",
    "bu" : "ba",
    "ku" : "ka",
    "gu" : "ga",
    "su" : "sa",
}
BASE_E = {
    "u" : "e",
    "tsu" : "te",
    "ru" : "re",
    "mu" : "me",
    "nu" : "ne",
    "bu" : "be",
    "ku" : "ke",
    "gu" : "ge",
    "su" : "se",
}
BASE_I = {
    "u" : "i",
    "tsu" : "chi",
    "ru" : "ri",
    "mu" : "mi",
    "nu" : "ni",
    "bu" : "bi",
    "ku" : "ki",
    "gu" : "gi",
    "su" : "shi",
}
BASE_O = {
    "u" : "o",
    "tsu" : "to",
    "ru" : "ro",
    "mu" : "mo",
    "nu" : "no",
    "bu" : "bo",
    "ku" : "ko",
    "gu" : "go",
    "su" : "so",
}
BASE_TA = {
    "u" : "tta",
    "tsu" : "tta",
    "ru" : "tta",
    "mu" : "nda",
    "nu" : "nda",
    "bu" : "nda",
    "ku" : "ita",
    "gu" : "ida",
    "su" : "shita",
}
BASE_TE = {
    "u" : "tte",
    "tsu" : "tte",
    "ru" : "tte",
    "mu" : "nde",
    "nu" : "nde",
    "bu" : "nde",
    "ku" : "ite",
    "gu" : "ide",
    "su" : "shite",
}
