import inflect
import os
import random

i = inflect.engine()

BASIC_CHOICES = {
    "rock": {
        "display": "r) Rock",
        "input": ("rock", "r"),
        "wins": {
            "lizard": "Rock crushes Lizard",
            "scissors": "Rock crushes Scissors",
        },
    },
    "paper": {
        "display": "p) Paper",
        "input": ("paper", "p"),
        "wins": {
            "rock": "Paper covers Rock",
            "spock": "Paper disproves Spock",
        },
    },
    "scissors": {
        "display": "c) Scissors",
        "input": ("scissors", "sc", "c", ),
        "wins": {
            "lizard": "Scissors decapitates Lizard",
            "paper": "Scissors cuts Paper",
        },
    },
}

EXTENDED_CHOICES = {
    "lizard": {
        "display": "l) Lizard",
        "input": ("lizard", "l"),
        "wins": {
            "paper": "Lizard eats Paper",
            "spock": "Lizard poisons Spock",
        },
    },
    "spock": {
        "display": "s) Spock",
        "input": ("spock", "sp", "s"),
        "wins": {
            "rock": "Spock vaporizes Rock",
            "scissors": "Spock smashes Scissors",
        },
    },
}


def prompt(message):
    print(f"==> {message}")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def game_version():

    clear_screen()
    prompt("Select the version of the game you want to play.")

    while True:
        prompt("Enter:\n")
        prompt("(C)lassic version: Rock, Paper, Scissors")
        prompt("(E)xtended version: Rock, Paper, Scissors, Lizard, Spock\n")
        version = input()
        if version.lower() in ["c", "classical"]:
            return BASIC_CHOICES
        elif version.lower() in ["e", "extended"]:
            return {**BASIC_CHOICES, **EXTENDED_CHOICES}
        else:
            prompt("Invalid choice!")


def get_player_choice(game_choices, valid_choices, display_choices):

    my_choice = ""

    while my_choice not in valid_choices:

        if my_choice != "":
            prompt("That's not a valid choice\n")
        prompt(f'Choose one:\n{"\n".join(display_choices)}')

        my_choice = input().lower()

        for key in valid_choices:
            if my_choice in game_choices[key]["input"]:
                my_choice = key
                break

    return my_choice


def get_computer_choice(valid_choices):
    return random.choice(list(valid_choices))


def display_match_winner(player_choice, computer_choice, game_choices):
    
    print()
    prompt(
        f"You chose {player_choice.capitalize()}, computer chose {computer_choice.capitalize()}\n"
    )

    if computer_choice in game_choices[player_choice]["wins"]:
        prompt(game_choices[player_choice]["wins"][computer_choice])
        prompt("You win!\n")
        winner = "player"
    elif player_choice in game_choices[computer_choice]["wins"]:
        prompt(game_choices[computer_choice]["wins"][player_choice])
        prompt("Computer wins!\n")
        winner = "computer"
    else:
        prompt("It's a tie!\n")
        winner = "tie"

    return winner


def play_again(message):
    while True:
        prompt(message)
        answer = input().lower()

        if answer.startswith('y') or answer.startswith('n'):
            return answer[0] == 'y'
        else:
            prompt("That's not a valid choice")


def play_round(game_choices, valid_choices, display_choices):
    player = get_player_choice(game_choices, valid_choices, display_choices)
    clear_screen()
    computer = get_computer_choice(valid_choices)
    winner = display_match_winner(player, computer, game_choices)
    return winner


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


def display_only(number_of_games):
    return f"only {number_of_games}" if number_of_games > 0 else "none"


def display_match(number_of_matches):
    return f"{number_of_matches} {i.plural('match', number_of_matches)}"


def play_game(game_choices, valid_choices, display_choices):
    number_of_matches = game_duration()
    total_matches = 0
    scores = {"player": 0, "computer": 0, "tie": 0}

    while True:
        
        if number_of_matches != 0:
            while total_matches < number_of_matches:
                game_winner = play_round(game_choices, valid_choices, display_choices)
                scores[game_winner] += 1
                total_matches += 1
        else:
            while True:
                game_winner = play_round(game_choices, valid_choices, display_choices)
                scores[game_winner] += 1
                total_matches += 1
                if not play_again("Do you want to play again [y/n]?"):
                    break

        if scores["player"] > scores["computer"]:
            prompt(f"You won {display_match(scores['player'])} out of {total_matches}, Computer won {display_only(scores['computer'])}")
            prompt("You are the final winner!\n")
            break
        elif scores["computer"] > scores["player"]:
            prompt(f"Computer won {display_match(scores['computer'])} out of {total_matches}, You won {display_only(scores['player'])}")
            prompt("Computer is the final winner!\n")
            break
        else:
            prompt(f"You won {display_match(scores['player'])} and computer won {display_match(scores['computer'])} out of {total_matches}")
            prompt("It's a tie!\n")
            if not play_again("Do you want to play an extra match to decide a winner? [y/n]"):
                break
            else:
                number_of_matches = total_matches + 1

    prompt("By!\n")


def main():
    game_choices = game_version()
    valid_choices = list(game_choices.keys())
    display_choices = [game_choices[key]["display"] for key in valid_choices]
    clear_screen()
    play_game(game_choices, valid_choices, display_choices)


if __name__ == "__main__":
    main()
