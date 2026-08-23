def get_base_a(verbe_parse: dict) -> str:
    base_a = {
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

    return base_a[verbe_parse["terminaison"]]


def get_base_e(verbe_parse: dict) -> str:
    base_e = {
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

    return base_e[verbe_parse["terminaison"]]


def get_base_i(verbe_parse: dict) -> str:
    base_i = {
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

    return base_i[verbe_parse["terminaison"]]


def get_base_o(verbe_parse: dict) -> str:
    base_o = {
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

    return base_o[verbe_parse["terminaison"]]


def get_base_ta(verbe_parse: dict) -> str:
    base_ta = {
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

    return base_ta[verbe_parse["terminaison"]]


def get_base_te(verbe_parse: dict) -> str:
    base_te = {
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

    return base_te[verbe_parse["terminaison"]]