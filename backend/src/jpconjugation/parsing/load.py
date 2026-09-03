from pathlib import Path
from jpconjugation.models import JPData

def load_json_file(file_path: str) -> JPData:
    file_content = Path(file_path).read_text(encoding="utf-8")

    return JPData.model_validate_json(file_content)