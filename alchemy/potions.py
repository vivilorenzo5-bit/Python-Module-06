from alchemy.elements import create_air, create_earth
import elements


def healing_potion() -> str:
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
    fire = elements.create_fire()
    water = elements.create_water()
    return f"Strength potion brewed with '{fire}' and '{water}'"
