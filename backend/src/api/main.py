import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jpconjugation.parsing.load import load_json_file
from api.models import GenerationOptions
from api.endpoints.options import get_conjugation_options
from api.endpoints.generate_conjugations import generate_conjugations

MAX_CONJUGATIONS = 50
try:
    data = load_json_file("./data/data.json")
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

@app.get("/api/options")
def get_options():
    return get_conjugation_options()


@app.post("/api/generate")
def generate(options: GenerationOptions):
    return generate_conjugations(data, options)
