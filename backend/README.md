# Backend
Utilise uv comme gertionnaire de paquets.
Utilise fastApi comme serveur.

## Setup
### Dépendences
```bash
uv sync
```

## Lancement
```bash
uv run fastapi dev src/api/main.py
```

## Mise à jour de data.json
```bash
uv run src/data_update/main.py <chemin/vers/fichierAnki.apkg>
```
