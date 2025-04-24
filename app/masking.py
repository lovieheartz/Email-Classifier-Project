# app/masking.py

import re
from app.config import ENTITY_TAGS
from app.constants import MASK_TAG_TEMPLATE

def mask_pii(text: str):
    """
    Replace PII entities with tag tokens in text.
    Returns masked text and list of entities with positions.
    """
    entities = []
    masked_text = text
    offset = 0  # Tracks how much the indices shift due to replacements

    # Collect matches first from original text
    all_matches = []

    for entity, pattern in ENTITY_TAGS.items():
        for match in re.finditer(pattern, text):
            start, end = match.span()
            original = match.group()
            all_matches.append({
                "entity": entity,
                "original": original,
                "start": start,
                "end": end
            })

    # Sort by start index to avoid index shift issues
    all_matches = sorted(all_matches, key=lambda x: x["start"])

    for match in all_matches:
        start = match["start"] + offset
        end = match["end"] + offset
        original = match["original"]
        entity = match["entity"]

        tag = MASK_TAG_TEMPLATE.format(entity=entity)
        masked_text = masked_text[:start] + tag + masked_text[end:]

        # Update offset for next match
        offset += len(tag) - (end - start)

        entities.append({
            "position": [start, start + len(tag)],
            "classification": entity,
            "entity": original
        })

    return masked_text, entities

def demask_text(masked_text: str, entities: list):
    """
    Replace tags with original PII values using position list.
    """
    sorted_entities = sorted(entities, key=lambda x: x['position'][0], reverse=True)
    for ent in sorted_entities:
        start, end = ent["position"]
        masked_text = masked_text[:start] + ent["entity"] + masked_text[end:]
    return masked_text

