import os
import random

GAME_RULES = {
    "rock": {
        "display": "(R)ock",
        "input": ("rock", "r"),
        "wins": {
            "lizard": "Rock crushes Lizard",
            "scissors": "Rock crushes Scissors",
        },
    },
    "paper": {
        "display": "(P)aper",
        "input": ("paper", "p"),
        "wins": {
            "rock": "Paper covers Rock",
            "spock": "Paper disproves Spock",
        },
    },
    "scissors": {
        "display": "S(c)issors",
        "input": ("scissors", "sc", "c", ),
        "wins": {
            "lizard": "Scissors decapitates Lizard",
            "paper": "Scissors cuts Paper",
        },
    },
    "lizard": {
        "display": "(L)izard",
        "input": ("lizard", "l"),
        "wins": {
            "paper": "Lizard eats Paper",
            "spock": "Lizard poisons Spock",
        },
    },
    "spock": {
        "display": "(S)pock",
        "input": ("spock", "sp", "s"),
        "wins": {
            "rock": "Spock vaporizes Rock",
            "scissors": "Spock smashes Scissors",
        },
    },
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

        if my_choice != "":
            prompt("That's not a valid choice\n")
        prompt(f'Choose one: {", ".join(DISPLAY_CHOICES)}')

        my_choice = input().lower()

        for key in VALID_CHOICES:
            if my_choice in GAME_RULES[key]["input"]:
                my_choice = key
                break

    return my_choice


def get_computer_choice():
    return random.choice(list(VALID_CHOICES))


def display_winner(player_choice, computer_choice):
    results = [0, 0, 0]
    print()
    prompt(
        f"You chose {player_choice.capitalize()}, computer chose {computer_choice.capitalize()}\n"
    )

    if computer_choice in GAME_RULES[player_choice]["wins"].keys():
        prompt(GAME_RULES[player_choice]["wins"][computer_choice])
        prompt(f"You win!\n")
        results[0] += 1
    elif player_choice in GAME_RULES[computer_choice]["wins"].keys():
        prompt(GAME_RULES[computer_choice]["wins"][player_choice])
        prompt(f"Computer wins!\n")
        results[1] += 1
    else:
        prompt(f"It's a tie!\n")
        results[2] += 1

    return results


def play_again(message):
    while True:
        prompt(message)
        answer = input().lower()

        if answer.startswith('y') or answer.startswith('n'):
            return answer[0] == 'y'
        else:
            prompt("That's not a valid choice")


def play_round(my_win, computer_win, tie):
    player = get_player_choice()
    computer = get_computer_choice()
    wins = display_winner(player, computer)
    return [my_win + wins[0], computer_win + wins[1], tie + wins[2]]


def game_duration():
    prompt("How many matches do you want to play? [0 for unlimited] ")
    while True:

        try:
            matches = int(input())
            if matches < 0:
                raise ValueError
            break
        except ValueError:
            prompt("Please enter an integer! [0 for unlimited matches] ")

    return matches


def main():
    clear_screen()
    number_of_matches = game_duration()
    total_matches = 0
    games_won = [0, 0, 0]

    while True:
        total_matches += 1
        if number_of_matches == 0:
            play_round()
            if not play_again("Do you want to play again (y/n)?"):
                break
            clear_screen()
        else:
            games_won = play_round(*games_won)
            number_of_matches -= 1
            if number_of_matches == 0:
                clear_screen()
                if games_won[0] > games_won[1]:
                    prompt(f"You won {games_won[0]} matches, computer won {games_won[1]} out of {total_matches} matches")
                    prompt(f"You are the final winner!\n")
                    break
                elif games_won[1] > games_won[0]:
                    prompt(f"You won only {games_won[0]} matches, computer won {games_won[1]} out of {total_matches} matches")
                    prompt(f"Computer is the final winner!\n")
                    break
                else:
                    prompt(f"You won {games_won[0]} matches, computer won {games_won[1]} out of {total_matches} matches")
                    prompt(f"It's a tie!\n")
                    if not play_again("Do you want to play an extra match to decide a winner? "):
                        break
                    number_of_matches = 1


if __name__ == "__main__":
    main()
