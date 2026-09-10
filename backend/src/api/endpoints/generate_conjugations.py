import random as rd

from fastapi import HTTPException
from jpconjugation.define import (
    VERBS_TENSES, VERBS_ALLOWED_FORMS,
    ADJECTIVES_TENSES, ADJECTIVES_ALLOWED_FORMS,
    FORMS
)
from jpconjugation.models import JPData
from jpconjugation.conjugation.verbs.conjugation import conjugate_verb, get_verb_rules
from jpconjugation.conjugation.adjectives.conjugation import conjugate_adjective, get_adjective_rules
from api.models import GenerationOptions, SectionSelection


def generate_conjugations(data: JPData, options: GenerationOptions) -> list:
    forms_section = options.sections.get("forms")
    verbs_section = options.sections.get("verbs")
    adjectives_section = options.sections.get("adjectives")

    if not forms_section:
        raise HTTPException(status_code=400, detail="Aucune combinaison possible avec ces filtres")

    # Get verbs and adjective according the options
    verbs, adjectives = _get_possible_verbs_adjectives(data, verbs_section, adjectives_section)

    # Compute all possible conjugations
    available_conjugations = []

    if verbs_section and verbs:
        for verb in verbs:
            for tense in verbs_section.values:
                verb_conjugations = conjugate_verb(verb, tense)
                if not verb_conjugations or len(verb_conjugations) == 0:
                    continue

                rules = get_verb_rules(verb, tense)

                for form in forms_section.values:
                    if not form in VERBS_ALLOWED_FORMS[tense]:
                        continue

                    result = verb_conjugations.get(form)
                    if not result:
                        continue

                    available_conjugations.append({
                        "romaji": verb.romaji,
                        "kanji": verb.kanji,
                        "traduction": verb.traduction,
                        "form": FORMS[form],
                        "tense": VERBS_TENSES[tense],
                        "rules": rules.get(form, "Missing rules"),
                        "result": result
                    })

    if adjectives_section and adjectives:
        for adjective in adjectives:
            for tense in adjectives_section.values:
                adjective_conjugations = conjugate_adjective(adjective, tense)
                if not adjective_conjugations or len(adjective_conjugations) == 0:
                    continue

                rules = get_adjective_rules(adjective, tense)

                for form in forms_section.values:
                    if not form in ADJECTIVES_ALLOWED_FORMS[tense]:
                        continue

                    result = adjective_conjugations.get(form)
                    if not result:
                        continue

                    available_conjugations.append({
                        "romaji": adjective.romaji,
                        "kanji": adjective.kanji,
                        "traduction": adjective.traduction,
                        "form": FORMS[form],
                        "tense": ADJECTIVES_TENSES[tense],
                        "rules": rules.get(form, "Missing rules"),
                        "result": result
                    })

    if not available_conjugations:
        raise HTTPException(status_code=400, detail="Aucune combinaison possible avec ces filtres")

    # Compute nb to generate
    nb_to_generate = min(options.number_conjugation, len(available_conjugations))

    # Suffle and get all conjugations
    return rd.sample(available_conjugations, nb_to_generate)


def _get_possible_verbs_adjectives(
        data: JPData,
        verbs_section: SectionSelection | None,
        adjectives_section: SectionSelection | None
        ) -> tuple[list, list]:
    verbs = []
    if verbs_section and len(verbs_section.types) != 0 and len(verbs_section.values) != 0:
        for verb in data.verbs:
            if verb.type in verbs_section.types:
                verbs.append(verb)

    adjectives = []
    if adjectives_section and len(adjectives_section.types) != 0 and len(adjectives_section.values) != 0:
        for adjective in data.adjectives:
            if adjective.type in adjectives_section.types:
                adjectives.append(adjective)

    return verbs, adjectives
