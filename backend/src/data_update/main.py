import os
import sys
import json
import zipfile
import sqlite3
import tempfile

from jpconjugation.parsing.load import load_data_json
from jpconjugation.models import Verb, Adjective
from jpconjugation.define import VERBS_TYPES, ADJECTIVES_TYPES
from data_update.parsing import clean_anki_html, get_word_parts_from_card
from data_update.jisho_api import (
    get_verb_type_from_jisho,
    get_adjective_type_from_jisho
)


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

    # Get new verbs and adjectives
    with tempfile.TemporaryDirectory() as tmpdir:
        # Unzip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Get db name
            if "collection.anki21" in zip_ref.namelist():
                db_name = "collection.anki21"
            else:
                db_name =  "collection.anki2"
            # Get db
            zip_ref.extract(db_name, tmpdir)
            db_path = os.path.join(tmpdir, db_name)

        # Connect to db
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Get deck data
        cursor.execute("SELECT decks FROM col LIMIT 1")
        decks_json = cursor.fetchone()[0]
        decks_data = json.loads(decks_json)

        # Build deck name dict from deck data
        deck_names = {int(deck_id): deck_info['name'] for deck_id, deck_info in decks_data.items()}

        # Get all card in verb and adjective deck
        cursor.execute("SELECT n.flds, c.did FROM notes as n LEFT JOIN cards as c ON n.id=c.nid")

        for row in cursor.fetchall():
            champs_carte = row[0].split('\x1f')
            deck_id = row[1]

            deck_name = deck_names.get(deck_id, "Unknown deck")

            recto = clean_anki_html(champs_carte[0]).strip()
            verso = clean_anki_html(champs_carte[1]).strip()

            if "2 - verbes" in deck_name.lower():
                parts = get_word_parts_from_card(recto, verso)
                if not parts:
                    continue
                kanji, romaji, traduction = parts

                if kanji in current_verbs:
                    continue

                type = get_verb_type_from_jisho(recto)
                if type not in VERBS_TYPES.keys():
                    continue

                print(f"Add {kanji}")
                nb_new_verbs += 1

                json_data.verbs.append(Verb(
                    kanji=kanji,
                    romaji=romaji,
                    type=type,
                    traduction=traduction))
                continue

            elif "3 - adjectifs" in deck_name.lower():
                parts = get_word_parts_from_card(recto, verso)
                if not parts:
                    continue
                kanji, romaji, traduction = parts

                if kanji in current_adjectives:
                    continue

                type = get_adjective_type_from_jisho(recto)
                if type not in ADJECTIVES_TYPES.keys():
                    continue

                print(f"Add {kanji}")
                nb_new_adjectives += 1

                json_data.adjectives.append(Adjective(
                        kanji=kanji,
                        romaji=romaji,
                        type=type,
                        traduction=traduction))
                continue

            else:
                continue

        conn.close()

    # Write new verbs and adjectives into data file
    json_string = json_data.model_dump_json(indent=4)

    with open("./data/data.json", "w", encoding="utf-8") as f:
        f.write(json_string)

    # Print update stats
    print(f"Added {nb_new_verbs} new verbs")
    print(f"Added {nb_new_adjectives} new adjectives")
