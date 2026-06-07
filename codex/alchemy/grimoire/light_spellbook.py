import alchemy
import elements
#from .light_validator import validate_ingredients

def light_spell_allowed_ingredients() -> list[str, str, str, str]:
    lst = []
    lst.append(alchemy.elements.create_earth())
    lst.append(alchemy.create_air())
    lst.append(elements.create_fire())
    lst.append(elements.create_water())
    return (lst)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    return(f'{spell_name} ({ingredients} - {validate_ingredients(ingredients)})')