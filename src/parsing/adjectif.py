def parse_conjugation_data(adjectif_data: dict) -> dict:
    adjectif = adjectif_data['romaji']

    # Get type
    type = adjectif_data.get("type", "")
    if type == "":
        if adjectif.endswith("i"):
            type = "i"
        else:
            type = "na"

    # Get radical
    radical = ""
    if type == "i":
        # Exception ii et kakkoii
        if adjectif in ["ii", "kakkoii"]:
            radical = adjectif[:-2] + "yo"
        else:
            radical = adjectif[:-1]

        return {
            "adjectif" : adjectif,
            "type" : type,
            "radical" : radical
        }

    return {
        "adjectif" : adjectif,
        "type" : type
    }