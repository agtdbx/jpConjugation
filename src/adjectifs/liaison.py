def get_liaison_i_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["radical"] + "kute"
    # Informel Négatif
    forme_in = adjectif_parse["radical"] + "kunakute"

    return {
        "ip" : forme_ip,
        "in" : forme_in,
    }


def get_liaison_na_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["adjectif"] + " de"
    # Informel Négatif
    forme_in = adjectif_parse["adjectif"] + " janakute"

    return {
        "ip" : forme_ip,
        "in" : forme_in,
    }