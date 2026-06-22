import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import_alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")

    try:
        print(f"Testing the hidden create_earth: {alchemy.create_earth()}")  # type: ignore
    except AttributeError as e:
        print(f"AttributeError caught successfully: {e}")
