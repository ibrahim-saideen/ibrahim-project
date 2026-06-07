import elements
import alchemy


def healing_potion() -> str:
    return (f'Healing potion brewed with '
            f'{alchemy.elements.create_earth()} element created and {alchemy.create_air()} element created')


def strength_potion() -> str:
    return (f'Strength potion brewed with '
            f'{elements.create_fire()} element created and {elements.create_water()} element created')
