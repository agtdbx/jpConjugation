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
    # Get verbs and adjective according the options
    verbs = []
    if len(options.verbs_types) != 0 and len(options.verbs_tense) != 0:
        for verb in data.verbs:
            if verb.type in options.verbs_types:
                verbs.append(verb)

    adjectives = []
    if len(options.adjectives_types) != 0 and len(options.adjectives_tense) != 0:
        for adjective in data.adjectives:
            if adjective.type in options.adjectives_types:
                adjectives.append(adjective)

    # Check which target is
    targets = []
    if len(verbs) != 0:
        targets.append("verb")
    if len(adjectives) != 0:
        targets.append("adjective")

    if len(targets) == 0:
        raise HTTPException(status_code=400, detail="Nothing to conjugate")

    conjugations = []

    for _ in range(options.number_conjugation):
        target = rd.choice(targets)

        if target == "verb":
            verb = rd.choice(verbs)
            form = rd.choice(options.forms)
            tense = rd.choice(options.verbs_tenses)

            result = conjugate_verb(verb, tense).get(form)

            conjugations.append({
                "target": verb.romaji,
                "form": FORMS[form],
                "tense": VERBS_TENSES[tense],
                "result": result
            })

        elif target == "adjective":
            adjective = rd.choice(adjectives)
            form = rd.choice(options.forms)
            tense = rd.choice(options.adjectives_tenses)

            result = conjugate_adjective(adjective, tense).get(form)

            conjugations.append({
                "target": adjective.romaji,
                "form": FORMS[form],
                "tense": ADJECTIVES_TENSES[tense],
                "result": result
            })

    return conjugations