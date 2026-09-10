import os
import json
import zipfile
import sqlite3
import tempfile

from typing import Iterator, Any
from data_update.parsing import clean_anki_html

def get_anki_cards_from_file(
        apkg_path: str
        ) -> Iterator[Any]:
    with tempfile.TemporaryDirectory() as tmpdir:
        # Unzip file
        with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
            # Get db name
            if "collection.anki21" in zip_ref.namelist():
                db_name = "collection.anki21"
            else:
                db_name =  "collection.anki2"
            # Get db
            zip_ref.extract(db_name, tmpdir)
            db_path = os.path.join(tmpdir, db_name)

        # Connect to db
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            # Get deck data
            cursor.execute("SELECT decks FROM col LIMIT 1")
            decks_data = json.loads(cursor.fetchone()[0])

            # Build deck name dict from deck data
            deck_names = {}
            for deck_id, deck_info in decks_data.items():
                deck_names[int(deck_id)] = deck_info['name']

            # Get number of cards
            cursor.execute("SELECT COUNT(*) FROM notes as n LEFT JOIN cards as c ON n.id=c.nid")
            total_cards = cursor.fetchone()[0]
            yield total_cards

            # Get all card in verb and adjective deck
            cursor.execute("SELECT n.flds, c.did FROM notes as n LEFT JOIN cards as c ON n.id=c.nid")

            # For each row
            for row in cursor:
                card_fields = row[0].split('\x1f')
                deck_id = row[1]

                # return card info, then continue from here next call
                yield {
                    "deck_name": deck_names.get(deck_id, "Unknown deck"),
                    "recto": clean_anki_html(card_fields[0]).strip(),
                    "verso": clean_anki_html(card_fields[1]).strip()
                }
