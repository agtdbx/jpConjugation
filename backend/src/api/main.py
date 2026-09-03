from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
            "verbs": {
                "title": "Verbes",
                "types": ["godan", "ichidan", "exception"],
                "tenses": ["pr", "pa", "im", "pro", "de-pr", "de-pa", "vo", "po"]
            },
            "adjectives": {
                "title": "Adjectifs",
                "types": ["ii", "na"],
                "tenses": ["pr", "pa", "co", "ad"]
            }
        }
    }