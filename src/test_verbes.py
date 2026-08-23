from parsing.load import load_json_file
from parsing.verbe import parse_conjugation_data
from verbes.present import  get_present_godan_formes, \
                            get_present_ichidan_formes, \
                            get_present_exception_formes
from verbes.passe import    get_passe_godan_formes, \
                            get_passe_ichidan_formes, \
                            get_passe_exception_formes
from verbes.imperatif import    get_imperatif_godan_formes, \
                                get_imperatif_ichidan_formes, \
                                get_imperatif_exception_formes
from verbes.progressif import   get_progressif_godan_formes, \
                                get_progressif_ichidan_formes, \
                                get_progressif_exception_formes
from verbes.volonte import  get_volonte_present_godan_formes, \
                            get_volonte_present_ichidan_formes, \
                            get_volonte_present_exception_formes, \
                            get_volonte_passe_godan_formes, \
                            get_volonte_passe_ichidan_formes, \
                            get_volonte_passe_exception_formes
from verbes.invitation import   get_invitation_godan_formes, \
                                get_invitation_ichidan_formes, \
                                get_invitation_exception_formes
from verbes.potentielle import  get_potentielle_godan_formes, \
                                get_potentielle_ichidan_formes, \
                                get_potentielle_exception_formes


if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/test.json")

    separator = "-" * 111

    print(separator)
    print(f"| {"Temps":15} | {"Informel Positif":20} | {"Formel Positif":20} | "+ \
          f"{"Informel Négatif":20} | {"Formel Négatif":20} |")
    print(separator)
    for verbe_data in json_data["verbes"]:

        verbe_parse = parse_conjugation_data(verbe_data)

        verbe = verbe_parse['verbe']
        terminaison = verbe_parse['terminaison']
        radical = verbe_parse['radical']

        for temps_id in ["pr", "pa", "im", "pro", "vo-pr", "vo-pa", "iv", "po"]:
            temps = ""
            forme_ip = ""
            forme_fp = ""
            forme_in = ""
            forme_fn = ""

            ##############################################################
            # Présent
            ##############################################################
            if temps_id == "pr":
                temps = "Présent"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_present_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_present_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_present_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Passé
            ##############################################################
            elif temps_id == "pa":
                temps = "Passé"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_passe_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_passe_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_passe_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Impératif
            ##############################################################
            elif temps_id == "im":
                temps = "Impératif"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_imperatif_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_imperatif_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_imperatif_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Progressif
            ##############################################################
            elif temps_id == "pro":
                temps = "Progressif"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_progressif_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_progressif_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_progressif_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Volonté présent
            ##############################################################
            elif temps_id == "vo-pr":
                temps = "Volonté présent"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_volonte_present_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_volonte_present_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_volonte_present_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Volonté passé
            ##############################################################
            elif temps_id == "vo-pa":
                temps = "Volonté passé"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_volonte_passe_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_volonte_passe_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_volonte_passe_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Invitation
            ##############################################################
            elif temps_id == "iv":
                temps = "Invitation"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_invitation_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_invitation_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_invitation_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            ##############################################################
            # Potentielle
            ##############################################################
            elif temps_id == "po":
                temps = "Potentielle"
                formes = {}
                if verbe_data["type"] == "godan":
                    formes = get_potentielle_godan_formes(verbe_parse)
                elif verbe_data["type"] == "ichidan":
                    formes = get_potentielle_ichidan_formes(verbe_parse)
                elif verbe_data["type"] == "exception":
                    formes = get_potentielle_exception_formes(verbe_parse)
                forme_ip = formes.get("ip", "")
                forme_fp = formes.get("fp", "")
                forme_in = formes.get("in", "")
                forme_fn = formes.get("fn", "")

            print(f"| {temps:15} | {forme_ip:20} | {forme_fp:20} | {forme_in:20} | {forme_fn:20} |")

        print(separator)