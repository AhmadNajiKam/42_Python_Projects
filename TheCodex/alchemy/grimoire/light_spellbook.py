def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "fire", "water", "wind"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    parsed_list: list[str] = validate_ingredients(ingredients).split(",")
    str_builder: str = ""
    size: int = len(parsed_list)
    i: int = 1
    while i < size:
        if i == size - 2:
            str_builder += parsed_list[i]
            str_builder += " and "
        elif i == size - 1:
            str_builder += parsed_list[i]
        else:
            str_builder += parsed_list[i]
            str_builder += ", "
        i += 1

    if parsed_list[0] == "VALID":
        return f"Spell recorded: {spell_name} ({str_builder} - VALID)"
    else:
        return f"Spell unrecorded: {spell_name} ({str_builder} - INVALID)"
