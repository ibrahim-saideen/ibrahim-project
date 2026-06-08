import elements
import alchemy


def healing_potion() -> str:
    return (f'Healing potion brewed with '
            f'{alchemy.elements.create_earth()} and {alchemy.create_air()}')


def strength_potion() -> str:
    return (f'Strength potion brewed with '
            f'{elements.create_fire()} and {elements.create_water()}')
