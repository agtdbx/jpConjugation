import json
import sqlite3
import zipfile
from data_update.anki_file import get_anki_cards_from_file

def test_get_anki_cards_from_file(tmp_path):
    # Create test db
    db_path = tmp_path / "collection.anki21"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create anki tables
    cursor.execute("CREATE TABLE col (decks TEXT)")
    cursor.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY, flds TEXT)")
    cursor.execute("CREATE TABLE cards (id INTEGER PRIMARY KEY, nid INTEGER, did INTEGER)")

    # Insert deck data
    fake_decks = {
        "1": {"name": "Deck Inconnu"},
        "2": {"name": "2 - verbes"}
    }
    cursor.execute("INSERT INTO col (decks) VALUES (?)", (json.dumps(fake_decks),))

    # Insert cards
    cursor.execute("INSERT INTO notes (id, flds) VALUES (1, 'recto1\x1fverso1')")
    cursor.execute("INSERT INTO notes (id, flds) VALUES (2, '食べる\x1f<div>manger</div>')")

    # Link cards and deck
    cursor.execute("INSERT INTO cards (id, nid, did) VALUES (1, 1, 1)")
    cursor.execute("INSERT INTO cards (id, nid, did) VALUES (2, 2, 2)")

    conn.commit()
    conn.close()

    # Zip db to an apkg file
    apkg_path = tmp_path / "test.apkg"
    with zipfile.ZipFile(apkg_path, 'w') as z:
        z.write(db_path, arcname="collection.anki21")

    # Begin test
    generator = get_anki_cards_from_file(str(apkg_path))

    # Check nb cards
    total_cards = next(generator)
    assert total_cards == 2

    # Get first card
    card1 = next(generator)
    assert card1["deck_name"] == "Deck Inconnu"
    assert card1["recto"] == "recto1"
    assert card1["verso"] == "verso1"

    # Get second card
    card2 = next(generator)
    assert card2["deck_name"] == "2 - verbes"
    assert card2["recto"] == "食べる"
    assert card2["verso"] == "manger"
