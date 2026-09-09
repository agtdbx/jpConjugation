from pydantic import BaseModel, PositiveInt, field_validator


class SectionSelection(BaseModel):
    types: list[str] = []
    values: list[str] = []


class GenerationOptions(BaseModel):
    number_conjugation: PositiveInt
    sections: dict[str, SectionSelection]
