import re
import html
import jaconv

def clean_anki_html(raw_text: str) -> str:
    if not raw_text:
        return ""

    # Convert html entities into chars (&nbsp;, &amp;, &lt;...)
    text = html.unescape(raw_text)

    # Replace <br> and <div> by \n
    text = text.replace('<br>', '\n').replace('<br/>', '\n').replace('<br />', '\n')
    text = text.replace('<div>', '\n').replace('</div>', '')

    # Remove other tag
    text = re.sub(r'<[^>]+>', '', text)

    # Replace multiple \n by only one \n
    text = re.sub(r'\n+', '\n', text).strip()

    return text


def _contains_kana(line: str) -> bool:
    return bool(re.search(r'[\u3040-\u309F\u30A0-\u30FF]', line))


def get_word_parts_from_card(recto: str, verso: str) -> tuple[str, str, str] | None:
    kanji = recto
    lines = verso.splitlines()
    if len(lines) == 0:
        return None
    elif len(lines) == 1:
        kana = recto
        traduction = lines[0].strip()
    else:
        if _contains_kana(lines[0].strip()):
            kana = lines[0].strip()
            traduction = lines[1].strip()
        else:
            kana = kanji
            traduction = lines[0].strip()
    romaji = jaconv.kana2alphabet(kana)

    return kanji, romaji, traduction
