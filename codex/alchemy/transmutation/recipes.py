import alchemy
from .. import potions
from elements import create_fire


def lead_to_gold() -> str:
    return (f'Recipe transmuting Lead to Gold:brew {alchemy.create_air()} element created '
            f'and {potions.strength_potion()} element created mixed with {create_fire()} element created')
