import os
import random

# VALID_CHOICES = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
CHOICE_BEATS = {
    "Rock": ("Lizard", "Scissors"),
    "Paper": ("Rock", "Spock"),
    "Scissors": ("Lizard", "Paper"),
    "Lizard": ("Paper", "Spock"),
    "Spock": ("Rock", "Scissors")
}

VALID_CHOICES = list(CHOICE_BEATS.keys())

def prompt(message):
    print(f"==> {message}")


def clear_screen():
    os.system("clear")


def get_player_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().capitalize()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    return choice


def get_computer_choice():
    return random.choice(VALID_CHOICES)


def display_winner(player_choice, computer_choice):
    prompt(f"You chose {player_choice}, computer chose {computer_choice}")

    if computer_choice in CHOICE_BEATS[player_choice]:
        print("You win!")
    elif player_choice in CHOICE_BEATS[computer_choice]:
        print("Computer wins!")
    else:
        print("It's a tie!")

    """
    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        prompt("You win!")
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")
    """


def play_again():
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('y') or answer.startswith('n'):
            return answer[0] == 'y'
        else:
            prompt("That's not a valid choice")


def play_round():
    clear_screen()
    player = get_player_choice()
    computer = get_computer_choice()
    display_winner(player, computer)


def main():
    while True:
        play_round()
        if not play_again():
            break


if __name__ == "__main__":
    main()
