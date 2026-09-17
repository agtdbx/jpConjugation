# jpConjugation

Une application web moderne et robuste pour maîtriser la conjugaison des verbes et adjectifs japonais, ainsi que leur vocabulaire associé.

## ✨ Fonctionnalités
- **Moteur de conjugaison exhaustif :** Gère parfaitement les verbes (Godan, Ichidan, exceptions absolues) et les adjectifs (i, na), en couvrant des nuances complexes comme la séparation des impératifs doux (requêtes) et durs (ordres secs).
- **Mutations Morphologiques & Chaînages :** Supporte les temps dérivés (désidératif, excès, conjecture). Le moteur gère nativement les mutations de classes grammaticales en cours de conjugaison (ex: un verbe mute en adjectif en i avec -tai, un adjectif mute en verbe avec -sugiru), permettant des combinaisons de temps dynamiques.
- **Génération sur mesure :** Créez des sessions d'exercices dynamiques en filtrant par temps, polarité (polie, neutre, négative) et type de mots, avec un respect strict des règles grammaticales japonaises.
- **Module de Référence Vocabulaire :** Intègre un dictionnaire et un lexique théorique complet. Les règles de conjugaison affichées sont calculées et générées dynamiquement par le backend pour éviter toute duplication de code.
- **Pipeline d'import Anki (ETL) :** Mettez à jour la base de vocabulaire en injectant directement vos paquets `.apkg`. Le script extrait les données SQLite à la volée via des générateurs (optimisation mémoire) et nettoie le HTML automatiquement.
- **Enrichissement par API :** Catégorise automatiquement les nouveaux mots importés en interrogeant Jisho.org pour déterminer leur classe grammaticale.
- **Tolérance de saisie :** L'interface normalise intelligemment les réponses de l'utilisateur (gestion des espaces multiples accidentels) et affiche l'explication de la règle grammaticale en cas d'erreur.
- **Architecture découplée :** Backend API strict validé par Pydantic V2, communiquant avec une interface React/TypeScript responsive.

## 🚀 Utilisation

**Côté Application Web :**
1. [Accédez à l'application](https://jp-conjugation-zeta.vercel.app/) depuis votre navigateur.
2. Naviguez entre l'onglet Conjugaison pour paramétrer vos exercices et l'onglet Vocabulaire pour consulter les règles théoriques et le dictionnaire.
3. Dans la configuration, choisissez le nombre de mots, le mode d'affichage (Kanji, Romaji, Traduction) et ciblez précisément les temps à réviser.
4. Cliquez sur **Passer aux exercices**.
5. Saisissez les conjugaisons demandées.

**Côté CLI (Import de vocabulaire) :**
Pour enrichir la base de données avec vos propres cartes mémoire, utilisez l'outil en ligne de commande intégré :
```bash
uv run src/data_update/main.py chemin/vers/votre_deck.apkg
```

## 🛠️ Développement et Tests
Ce projet applique une séparation stricte des environnements, gérés de manière moderne.

### Backend (Python / FastAPI)
Le backend utilise uv pour la gestion des dépendances. La fiabilité du moteur linguistique est garantie par du Black-Box Testing exhaustif : l'intégralité des règles est testée via des matrices de données paramétrées avec `pytest`.

```bash
# Setup
cd backend
uv sync

# Lancer le serveur local
uv run fastapi dev src/api/main.py

# Lancer la suite de tests unitaires (avec pytest-mock et tmp_path)
uv run pytest src/tests
```

### Frontend (React / Vite)
L'interface utilisateur est développée en TypeScript, garantissant un typage fort des modèles de données reçus de l'API.

```bash
# Setup
cd frontend
npm ci
cp .env.example .env

# Lancer le client local
npm run dev
```

### Intégration Continue (CI)
Le dépôt est sécurisé par un pipeline GitHub Actions parallèle. À chaque push sur `master`, la CI vérifie indépendamment :
- **Backend** : Cache uv, installation propre, et validation à 100% de la suite `pytest`.
- **Frontend** : Cache Node, lintage (`ESLint`), vérification stricte des types (`tsc --noEmit`), et test de build.


## 👥 Auteur
**Auguste Deroubaix** (agtdbx) 🔗 [GitHub](https://github.com/agtdbx)
