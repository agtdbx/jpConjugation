import sys
import random as rd

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from jpconjugation.define import (
    VERBS_TYPES, VERBS_TENSES,
    ADJECTIVES_TYPES, ADJECTIVES_TENSES,
    FORMS
)
from jpconjugation.parsing.load import load_json_file
from jpconjugation.conjugation.verbs.conjugation import conjugate_verb
from jpconjugation.conjugation.adjectives.conjugation import conjugate_adjective
from api.models import GenerationOptions

MAX_CONJUGATIONS = 50
try:
    data = load_json_file("./data/data.json")
except Exception as e:
    print(f"Error : {e}")
    sys.exit()
else:
    print("Data loaded")

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://jp-conjugation-zeta.vercel.app"
    ],  # Allow React local app and vercel app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/options")
def get_options():
    return {
        "sections": {
            "forms": {
                "title": "Formes",
                "types": {},
                "values": FORMS
            },
            "verbs": {
                "title": "Verbes",
                "types": VERBS_TYPES,
                "values": VERBS_TENSES
            },
            "adjectives": {
                "title": "Adjectifs",
                "types": ADJECTIVES_TYPES,
                "values": ADJECTIVES_TENSES
            }
        }
    }


@app.post("/api/generate")
def generate_conjugation(options: GenerationOptions):
    forms_section = options.sections.get("forms")
    verbs_section = options.sections.get("verbs")
    adjectives_section = options.sections.get("adjectives")

    # Get verbs and adjective according the options
    verbs = []
    if len(verbs_section.types) != 0 and len(verbs_section.values) != 0:
        for verb in data.verbs:
            if verb.type in verbs_section.types:
                verbs.append(verb)

    adjectives = []
    if len(adjectives_section.types) != 0 and len(adjectives_section.values) != 0:
        for adjective in data.adjectives:
            if adjective.type in adjectives_section.types:
                adjectives.append(adjective)

    # Compute all possible combinations
    available_combinations = []

    if verbs_section and verbs:
        for verb in verbs:
            for form in forms_section.values:
                for tense in verbs_section.values:
                    available_combinations.append(("verb", verb, form, tense))

    if adjectives_section and adjectives:
        for adjective in adjectives:
            for form in forms_section.values:
                for tense in adjectives_section.values:
                    available_combinations.append(("adjective", adjective, form, tense))

    if not available_combinations:
        raise HTTPException(status_code=400, detail="Aucune combinaison possible avec ces filtres")

    # Compute nb to generate
    nb_to_generate = min(options.number_conjugation, len(available_combinations))

    # Suffle and get all combinations
    selected_combinations = rd.sample(available_combinations, nb_to_generate)

    conjugations = []

    for target_type, word, form, tense in selected_combinations:

        if target_type == "verb":
            result = conjugate_verb(word, tense).get(form)

            conjugations.append({
                "target": word.romaji,
                "form": FORMS[form],
                "tense": VERBS_TENSES[tense],
                "result": result
            })

        elif target_type == "adjective":
            result = conjugate_adjective(word, tense).get(form)

            conjugations.append({
                "target": word.romaji,
                "form": FORMS[form],
                "tense": ADJECTIVES_TENSES[tense],
                "result": result
            })

    return conjugations