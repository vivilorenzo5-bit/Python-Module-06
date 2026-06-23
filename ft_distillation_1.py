import alchemy
import alchemy.potions


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")

    s_potion = alchemy.potions.strength_potion()
    print(f"Testing strength_potion: {s_potion}")

    h_potion = alchemy.heal()
    print(f"Testing heal alias: {h_potion}")
