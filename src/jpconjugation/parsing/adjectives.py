def parse_conjugation_data(adjectif_data: dict) -> dict:
    adjectif = adjectif_data['romaji']

    # Get type
    type = adjectif_data.get("type", "")
    if type == "":
        if adjectif.endswith("i"):
            type = "i"
        else:
            type = "na"

    # Get stem
    stem = ""
    if type == "i":
        # Exception ii et kakkoii
        if adjectif in ["ii", "kakkoii"]:
            stem = adjectif[:-2] + "yo"
        else:
            stem = adjectif[:-1]

        return {
            "adjectif" : adjectif,
            "type" : type,
            "stem" : stem
        }

    return {
        "adjectif" : adjectif,
        "type" : type
    }