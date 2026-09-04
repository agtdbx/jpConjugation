from pydantic import BaseModel, PositiveInt, field_validator
from jpconjugation.define import (
    FORMS, VERBS_TENSES, VERBS_TYPES,
    ADJECTIVES_TENSES, ADJECTIVES_TYPES
)

# class GenerationOptionsForm(BaseModel):
#     types: list[str] = []
#     values: list[str]

#     @field_validator('values')
#     @classmethod
#     def validate_forms_values(cls, values):
#         for v in values:
#             if v not in FORMS:
#                 raise ValueError(f"Forme invalide: {v}. Autorisées: {list(FORMS.keys())}")
#         return values


# class GenerationOptionsVerb(BaseModel):
#     types: list[str]
#     values: list[str]

#     @field_validator('types')
#     @classmethod
#     def validate_verbs_types(cls, values):
#         for v in values:
#             if v not in VERBS_TYPES:
#                 raise ValueError(f"Type de verbe invalide: {v}")
#         return values

#     @field_validator('values')
#     @classmethod
#     def validate_verbs_values(cls, values):
#         for v in values:
#             if v not in VERBS_TENSES:
#                 raise ValueError(f"Temps de verbe invalide: {v}")
#         return values


# class GenerationOptionsAdjectives(BaseModel):
#     types: list[str]
#     values: list[str]

#     @field_validator('types')
#     @classmethod
#     def validate_adjectives_types(cls, values):
#         for v in values:
#             if v not in ADJECTIVES_TYPES:
#                 raise ValueError(f"Type d'adjectif invalide: {v}")
#         return values

#     @field_validator('values')
#     @classmethod
#     def validate_adjectives_values(cls, values):
#         for v in values:
#             if v not in ADJECTIVES_TENSES:
#                 raise ValueError(f"Temps d'adjectif invalide: {v}")
#         return values


# class SectionsSelection(BaseModel):
#     forms: GenerationOptionsForm
#     verbs: GenerationOptionsVerb
#     adjectives: GenerationOptionsAdjectives


# class GenerationOptions(BaseModel):
#     number_conjugation: PositiveInt
#     sections: SectionsSelection


class SectionSelection(BaseModel):
    types: list[str] = []
    values: list[str] = []


class GenerationOptions(BaseModel):
    number_conjugation: PositiveInt
    sections: dict[str, SectionSelection]