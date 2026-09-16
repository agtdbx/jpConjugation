from pydantic import BaseModel, PositiveInt


class CategorySelection(BaseModel):
    types: list[str] = []
    tenses: list[str] = []


class GenerationOptions(BaseModel):
    numberConjugation: PositiveInt
    forms: list[str] = []
    categories: dict[str, CategorySelection]
