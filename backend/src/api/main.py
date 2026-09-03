from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jpconjugation.define import    VERBS_TYPES, VERBS_TENSES, VERBS_TENSES_NAME,\
                                    ADJECTIVES_TYPES, ADJECTIVES_TENSES, AJDJECTIVES_TENSES_NAME

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
                "types": VERBS_TYPES,
                "tenses": VERBS_TENSES,
                "names": VERBS_TENSES_NAME
            },
            "adjectives": {
                "title": "Adjectifs",
                "types": ADJECTIVES_TYPES,
                "tenses": ADJECTIVES_TENSES,
                "names": AJDJECTIVES_TENSES_NAME
            }
        }
    }