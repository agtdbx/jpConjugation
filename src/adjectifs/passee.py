def get_passee_i_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["radical"] + "katta"
    # Informel Négatif
    forme_in = adjectif_parse["radical"] + "kunakatta"

    return {
        "ip" : forme_ip,
        "fp" : f"{forme_ip} desu",
        "in" : forme_in,
        "fn" : f"{forme_in} desu",
    }


def get_passee_na_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["adjectif"] + " datta"
    # Formel Positif
    forme_fp = adjectif_parse["adjectif"] + " deshita"
    # Informel Négatif
    forme_in = adjectif_parse["adjectif"] + " janakatta"
    # Formel Négatif
    forme_fn = adjectif_parse["adjectif"] + " ja arimasen deshita"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }