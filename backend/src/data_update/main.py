import sys
from tqdm import tqdm
from jpconjugation.parsing.load import load_data_json
from data_update.parsing import clean_anki_html
from data_update.verbs import get_verb_if_needed
from data_update.adjectives import get_adjective_if_needed
from data_update.anki_file import get_anki_cards_from_file

if __name__ == "__main__":
    # Check number of parameter
    if len(sys.argv) != 2:
        print("Missing: parameter\n" + \
              "Usage: uv run src/data_update/main.py <path/to/ankiFile.apkg>")
        sys.exit()

    # Check file extension
    file_path = sys.argv[1]
    if not file_path.endswith('.apkg'):
        print(f"Error: input file must be an anki file")
        sys.exit()

    # Get and parse json data
    try:
        json_data = load_data_json()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

    # Get existing verbs and adjectives
    current_verbs = set()
    for verb in json_data.verbs:
        current_verbs.add(verb.kanji)

    current_adjectives = set()
    for adjective in json_data.adjectives:
        current_adjectives.add(adjective.kanji)

    nb_new_verbs = 0
    nb_new_adjectives = 0

    # Init card generator
    card_generator = get_anki_cards_from_file(file_path)

    # Get number of cards
    cards_number = next(card_generator)

    # Setup progress bar
    with tqdm(total=cards_number, desc="Import Anki", unit="carte") as pbar:
        # Get new verbs and adjectives
        for card in card_generator:
            # Update progress bar
            pbar.update(1)

            deck_name = card["deck_name"]
            recto = card["recto"]
            verso = card["verso"]

            added_word = None

            if "2 - verbes" in deck_name.lower():
                verb = get_verb_if_needed(current_verbs, recto, verso)
                if not verb:
                    continue

                nb_new_verbs += 1
                added_word = verb.kanji

                json_data.verbs.append(verb)

            elif "3 - adjectifs" in deck_name.lower():
                adjective = get_adjective_if_needed(current_adjectives, recto, verso)
                if not adjective:
                    continue

                nb_new_adjectives += 1
                added_word = adjective.kanji

                json_data.adjectives.append(adjective)

            if added_word:
                pbar.set_postfix_str(f"Dernier ajout: {added_word}")

    # Write new verbs and adjectives into data file
    json_string = json_data.model_dump_json(indent=4)

    with open("./data/data.json", "w", encoding="utf-8") as f:
        f.write(json_string)

    # Print update stats
    print(f"Added {nb_new_verbs} new verbs")
    print(f"Added {nb_new_adjectives} new adjectives")
