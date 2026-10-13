import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def decide_winner(player, computer):
    if player == computer:
        return "tie"

    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"


def main():
    player_score = 0
    computer_score = 0
    ties = 0

    print("\n===== ROCK, PAPER, SCISSORS =====")
    print("Type rock, paper, or scissors.")
    print("Type q to quit.\n")

    while True:
        player = input("Your choice: ").strip().lower()

        if player == "q":
            break

        if player not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.\n")
            continue

        computer = get_computer_choice()
        print("Computer chose:", computer)

        result = decide_winner(player, computer)

        if result == "tie":
            print("It's a tie!")
            ties += 1
        elif result == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(
            f"Score — You: {player_score}, "
            f"Computer: {computer_score}, Ties: {ties}\n"
        )

    print("\n===== FINAL SCORE =====")
    print("Your wins:", player_score)
    print("Computer wins:", computer_score)
    print("Ties:", ties)
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
