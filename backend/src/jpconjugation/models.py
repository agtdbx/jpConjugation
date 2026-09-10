from pydantic import BaseModel, Field, field_validator, model_validator
from jpconjugation.define import (
    VERBS_TYPES, VERBS_ENDINGS,
    ADJECTIVES_TYPES, ADJECTIVES_EXCEPTIONS
)

class Verb(BaseModel):
    romaji: str = Field(..., min_length=1)
    kanji: str = Field(..., min_length=1)
    traduction: str = Field(..., min_length=1)
    type: str = Field(..., min_length=1)
    stem: str = ""
    ending: str = ""

    @field_validator('type')
    @classmethod
    def validate_forms(cls, value):
        if value not in VERBS_TYPES:
            raise ValueError(f"Type invalide: {value}. Autorisées: {list(VERBS_TYPES.keys())}")
        return value

    # Compute fields if needed
    @model_validator(mode='after')
    def compute_stem_and_ending(self):
        if not self.ending:
            for term in VERBS_ENDINGS:
                if self.romaji.endswith(term):
                    self.ending = term
                    break

        if not self.ending:
            raise ValueError(f"Aucune terminaison trouvée pour le verbe '{self.romaji}'")

        if not self.stem:
            self.stem = self.romaji[:-len(self.ending)]

        return self


class Adjective(BaseModel):
    romaji: str = Field(..., min_length=1)
    kanji: str = Field(..., min_length=1)
    traduction: str = Field(..., min_length=1)
    type: str = Field(..., min_length=1)

    @field_validator('type')
    @classmethod
    def validate_type(cls, value):
        if value not in ADJECTIVES_TYPES:
            raise ValueError(f"Type invalide: {value}. Autorisés: {list(ADJECTIVES_TYPES.keys())}")
        return value

    stem: str = ""

    @model_validator(mode='after')
    def compute_type_and_stem(self):
        if not self.type:
            self.type = "i" if self.romaji.endswith("i") else "na"

        if self.type == "i":
            if self.romaji in ADJECTIVES_EXCEPTIONS.keys():
                self.stem = ADJECTIVES_EXCEPTIONS[self.romaji]
            else:
                self.stem = self.romaji[:-1]
        else:
            self.stem = self.romaji

        return self


class JPData(BaseModel):
    verbs: list[Verb]
    adjectives: list[Adjective]
