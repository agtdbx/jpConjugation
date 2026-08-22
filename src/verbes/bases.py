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