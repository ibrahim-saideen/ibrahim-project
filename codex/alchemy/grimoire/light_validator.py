from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    ingredients.lower()
    lst = light_spell_allowed_ingredients()
    for i in range(4):
        if lst[i].lower() in ingredients:
            return ('VALID')
    return ('INVALID')
