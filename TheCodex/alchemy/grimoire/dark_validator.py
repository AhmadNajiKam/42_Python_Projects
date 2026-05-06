from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_list: list[str] = ingredients.split(",")
    valid_list: list[str] = dark_spell_allowed_ingredients()
    for item in ingredients_list:
        if item.lower() not in valid_list:
            return f"INVALID,{ingredients}"
    return f"VALID,{ingredients}"
