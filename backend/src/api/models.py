from pydantic import BaseModel, PositiveInt, field_validator
from jpconjugation.define import (
    FORMS, VERBS_TENSES, VERBS_TYPES,
    ADJECTIVES_TENSES, ADJECTIVES_TYPES
)


class GenerationOptions(BaseModel):
    number_conjugation: PositiveInt
    forms: list[str]
    verbs_types: list[str]
    verbs_tenses: list[str]
    adjectives_types: list[str]
    adjectives_tenses: list[str]

    @field_validator('forms')
    @classmethod
    def validate_forms(cls, values):
        for v in values:
            if v not in FORMS:
                raise ValueError(f"Forme invalide: {v}. Autorisées: {list(FORMS.keys())}")
        return values

    @field_validator('verbs_tenses')
    @classmethod
    def validate_verbs_tenses(cls, values):
        for v in values:
            if v not in VERBS_TENSES:
                raise ValueError(f"Temps de verbe invalide: {v}")
        return values

    @field_validator('verbs_types')
    @classmethod
    def validate_verbs_types(cls, values):
        for v in values:
            if v not in VERBS_TYPES:
                raise ValueError(f"Type de verbe invalide: {v}")
        return values

    @field_validator('adjectives_tenses')
    @classmethod
    def validate_adj_tenses(cls, values):
        for v in values:
            if v not in ADJECTIVES_TENSES:
                raise ValueError(f"Temps d'adjectif invalide: {v}")
        return values

    @field_validator('adjectives_types')
    @classmethod
    def validate_adj_types(cls, values):
        for v in values:
            if v not in ADJECTIVES_TYPES:
                raise ValueError(f"Type d'adjectif invalide: {v}")
        return values