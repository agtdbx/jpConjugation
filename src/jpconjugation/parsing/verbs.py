def parse_conjugation_data(verbe_data: dict) -> dict:
    verbe = verbe_data['romaji']

    # Get ending
    ending = ""
    for term in ["tsu", "ru", "mu", "nu", "bu", "ku", "gu", "su", "u"]:
        if verbe.endswith(term):
            ending = term
            break

    if ending == "":
        raise RuntimeError("No ending found")

    # Get stem
    stem = verbe[:-len(ending)]

    return {
        "verbe" : verbe,
        "ending" : ending,
        "stem" : stem,
        "type": verbe_data['type']
    }