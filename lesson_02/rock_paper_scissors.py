import os
import random

GAME_RULES = {
    "rock": {
        "display": "(R)ock",
        "input": ("rock", "r"),
        "wins": ("lizard", "scissors")
    },
    "paper": {
        "display": "(P)aper",
        "input": ("paper", "p"),
        "wins": ("rock", "spock")
    },
    "scissors": {
        "display": "S(c)issors",
        "input": ("scissors", "sc", "c", ),
        "wins": ("lizard", "paper")
    },
    "lizard": {
        "display": "(L)izard",
        "input": ("lizard", "l"),
        "wins": ("paper", "spock")
    },
    "spock": {
        "display": "(S)pock",
        "input": ("spock", "sp", "s"),
        "wins": ("rock", "scissors")
    }
}

VALID_CHOICES = GAME_RULES.keys()
DISPLAY_CHOICES = list(GAME_RULES[key]["display"] for key in VALID_CHOICES)


def prompt(message):
    print(f"==> {message}")


def clear_screen():
    os.system("clear")


def get_player_choice():

    my_choice = ""

    while my_choice not in VALID_CHOICES:

        if my_choice !="":
            prompt("That's not a valid choice\n")
        prompt(f'Choose one: {", ".join(DISPLAY_CHOICES)}')

        choice = input().lower()

        for key in VALID_CHOICES:
            if choice in GAME_RULES[key]["input"]:
                my_choice = key
                break

    return my_choice


def get_computer_choice():
    return random.choice(list(VALID_CHOICES))


def display_winner(player_choice, computer_choice):
    print()
    prompt(f"You chose {player_choice}, computer chose {computer_choice}\n")

    if computer_choice in GAME_RULES[player_choice]["wins"]:
        prompt(f"You win!\n")
    elif player_choice in GAME_RULES[computer_choice]["wins"]:
        prompt(f"Computer wins!\n")
    else:
        prompt(f"It's a tie!\n")


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
