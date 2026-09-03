from pydantic import BaseModel, Field, model_validator
from typing import Literal, Optional

class Verb(BaseModel):
    romaji: str = Field(..., min_length=1)
    kanji: str = Field(..., min_length=1)
    traduction: str = Field(..., min_length=1)

    # Check if type is one of thoses
    type: Literal["godan", "ichidan", "exception"]

    # Fields to compute
    stem: str = ""
    ending: str = ""

    # How to compute fields
    @model_validator(mode='after')
    def compute_stem_and_ending(self):
        for term in ["tsu", "ru", "mu", "nu", "bu", "ku", "gu", "su", "u"]:
            if self.romaji.endswith(term):
                self.ending = term
                break

        if not self.ending:
            raise ValueError(f"Aucune terminaison trouvée pour le verbe '{self.romaji}'")

        self.stem = self.romaji[:-len(self.ending)]
        return self


class Adjective(BaseModel):
    romaji: str = Field(..., min_length=1)
    kanji: str = Field(..., min_length=1)
    traduction: str = Field(..., min_length=1)
    type: Optional[Literal["ii", "na"]] = None

    stem: str = ""

    @model_validator(mode='after')
    def compute_type_and_stem(self):
        if not self.type:
            self.type = "ii" if self.romaji.endswith("i") else "na"

        if self.type == "ii":
            if self.romaji in ["ii", "kakkoii"]:
                self.stem = self.romaji[:-2] + "yo"
            else:
                self.stem = self.romaji[:-1]
        else:
            self.stem = self.romaji

        return self


class JPData(BaseModel):
    verbs: list[Verb]
    adjectives: list[Adjective]