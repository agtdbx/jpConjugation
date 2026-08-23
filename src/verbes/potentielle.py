from verbes.bases import get_base_e

def get_potentielle_godan_formes(verbe_parse: dict) -> dict:
    base_e = get_base_e(verbe_parse)

    # Informel Positif
    forme_ip = verbe_parse["radical"] + base_e + "ru"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + base_e + "masu"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + base_e + "nai"
    # Formel Négatif
    forme_fn = verbe_parse["radical"] + base_e + "masen"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }


def get_potentielle_ichidan_formes(verbe_parse: dict) -> dict:
    # Informel Positif
    forme_ip = verbe_parse["radical"] + "rareru"
    # Formel Positif
    forme_fp = verbe_parse["radical"] + "raremasu"
    # Informel Négatif
    forme_in = verbe_parse["radical"] + "rarenai"
    # Formel Négatif
    forme_fn = verbe_parse["radical"] + "raremasen"

    return {
        "ip" : forme_ip,
        "fp" : forme_fp,
        "in" : forme_in,
        "fn" : forme_fn,
    }


def get_potentielle_exception_formes(verbe_parse: dict) -> dict:
    if verbe_parse["verbe"] == "iku":
        return get_potentielle_godan_formes(verbe_parse)
    elif verbe_parse["verbe"] == "suru":
        return {
            "ip" : "dekiru",
            "fp" : "dekimasu",
            "in" : "dekinai",
            "fn" : "dekimasen",
        }
    elif verbe_parse["verbe"] == "kuru":
        return {
            "ip" : "korareru",
            "fp" : "koraremasu",
            "in" : "korarenai",
            "fn" : "koraremasen",
        }

    return {}