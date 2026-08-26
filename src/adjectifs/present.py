def get_present_i_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["adjectif"]
    # Informel Négatif
    forme_in = adjectif_parse["radical"] + "kunai"

    return {
        "ip" : forme_ip,
        "fp" : f"{forme_ip} desu",
        "in" : forme_in,
        "fn" : f"{forme_in} desu",
    }


def get_present_na_formes(adjectif_parse: dict) -> dict:
    # Informel Positif
    forme_ip = adjectif_parse["adjectif"] + " da"
    # Formel Positif
    forme_fp = adjectif_parse["adjectif"] + " desu"
    # Informel Négatif
    forme_in = adjectif_parse["adjectif"] + " janai"
    # Formel Négatif
    forme_fn = adjectif_parse["adjectif"] + " ja arimasen"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }