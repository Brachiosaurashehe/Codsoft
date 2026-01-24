import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")


def get_complexity():
    print("\nChoose password complexity:")
    print("1. Letters only")
    print("2. Letters and numbers")
    print("3. Letters, numbers, and symbols")

    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def generate_password(length, complexity):
    if complexity == "1":
        characters = string.ascii_letters
    elif complexity == "2":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("===== PASSWORD GENERATOR =====")

    length = get_password_length()
    complexity = get_complexity()

    password = generate_password(length, complexity)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()