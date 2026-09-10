from pathlib import Path
from jpconjugation.define import DATA_FILE_PATH
from jpconjugation.models import JPData

def load_data_json(file_path: str = DATA_FILE_PATH) -> JPData:
    file_content = Path(file_path).read_text(encoding="utf-8")

    return JPData.model_validate_json(file_content)
