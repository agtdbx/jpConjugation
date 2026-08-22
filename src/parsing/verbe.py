def parse_conjugation_data(verbe_data: dict) -> dict:
    verbe = verbe_data['romaji']

    # Get terminaison
    terminaison = ""
    for term in ["tsu", "ru", "mu", "nu", "bu", "ku", "gu", "su", "u"]:
        if verbe.endswith(term):
            terminaison = term
            break

    if terminaison == "":
        raise RuntimeError("No terminaison found")

    # Get radical
    radical = verbe[:-len(terminaison)]

    return {
        "verbe" : verbe,
        "terminaison" : terminaison,
        "radical" : radical,
    }