def main() -> None:
    from models import Person

    p1 = Person("Naruto", "Uzumaki")
    print(f"My name is {p1.first_name} {p1.last_name}!")


if __name__ == "__main__":
    main()
