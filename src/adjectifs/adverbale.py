def get_adverbale_i_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["radical"] + "ku"

    return {
        "ip" : forme_ip
    }


def get_adverbale_na_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["adjectif"] + " ni"

    return {
        "ip" : forme_ip
    }