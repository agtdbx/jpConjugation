import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jpconjugation.parsing.load import load_data_json
from api.models import GenerationOptions
from api.conjugation.options import get_conjugation_options
from api.conjugation.generate_conjugations import generate_conjugations
from api.vocabulary.data import get_vocabulary_data

MAX_CONJUGATIONS = 50
try:
    data = load_data_json("./data/data.json")
except Exception as e:
    print(f"Error: {e}")
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

@app.get("/api/conjugation/options")
def conjugation_options():
    return get_conjugation_options()


@app.post("/api/conjugation/generate")
def conjugation_generate(options: GenerationOptions):
    return generate_conjugations(data, options)


@app.get("/api/vocabulary")
def vocabulary_data():
    return get_vocabulary_data(data)
