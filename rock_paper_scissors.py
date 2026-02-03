import random


def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"


def main():
    user_score = 0
    computer_score = 0

    print("===== ROCK PAPER SCISSORS GAME =====")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()