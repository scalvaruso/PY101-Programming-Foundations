import os               # Used for clearing the terminal
import random           # Used for computer choice
import socket           # Used to get computer (host) name
import inflect          # Library for pluralization (e.g., match → matches)

i = inflect.engine()    # Create pluralization engine


# Standardised prompt output function
def prompt(message, end="\n"):
    print(f"==> {message}", end=end)


# Clears terminal screen depending on OS (Windows vs Unix)
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Gets player name and computer (hostname)
def get_players_name():
    clear_screen()
    print()
    hostname = socket.gethostname()  # Computer name
    prompt(f"Hi, my name is {hostname}\n")
    prompt("Please enter your name:\n")
    player = input()
    return player, hostname


# Lets user choose between classic and extended game versions
def select_game_version(player):

    # Base game: Rock, Paper, Scissors
    basic_choices = {
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
            "input": ("scissors", "sc", "c"),
            "wins": {
                "lizard": "Scissors decapitates Lizard",
                "paper": "Scissors cuts Paper",
            },
        },
    }

    # Extra options for extended version
    extended_choices = {
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

    clear_screen()
    print()
    prompt(f"Hi {player}")
    print()
    prompt("Select the version of the game you want to play.\n")

    # Loop until valid input
    while True:
        prompt("(C) - Classic version : Rock, Paper, Scissors")
        prompt("(E) - Extended version: "
               "Rock, Paper, Scissors, Lizard, Spock\n")
        version = input()

        if version.lower() in ["c", "classical"]:
            return basic_choices
        if version.lower() in ["e", "extended"]:
            # Merge dictionaries for extended version
            return {**basic_choices, **extended_choices}

        clear_screen()
        print("\n")
        prompt(f"{version} is an invalid choice! Please select:\n")


# Ask user how many matches to play
def select_game_duration():
    clear_screen()
    print()
    prompt("How many matches do you want to play? [0 for unlimited] ", "")

    while True:
        try:
            matches = int(input())  # Convert input to integer
            if matches < 0:
                raise ValueError   # Reject negative numbers
            break
        except ValueError:
            clear_screen()
            print()
            prompt("Please enter an integer! [0 for unlimited matches] ", "")

    return matches


# Ask user a yes/no question and return True/False
def play_again(message):
    while True:
        prompt(f"{message}", "")
        answer = input().lower()

        if answer.startswith('y') or answer.startswith('n'):
            return answer[0] == 'y'   # True if 'y', False if 'n'

        clear_screen()
        print()
        prompt("That's not a valid choice")
        print("\n"*4)


# Display helper: show "only X" or "none"
def display_only(number_of_games):
    return f"only {number_of_games}" if number_of_games > 0 else "none"


# Pluralise a word based on quantity
def make_plural(item, quantity):
    return f"{i.plural(item, quantity)}"


# Format "X match/matches"
def match_plural(quantity):
    return f"{quantity} {make_plural('match', quantity)}"


# Get player's choice with validation
def get_player_choice(game_choices, valid_choices, display_choices):

    my_choice = None

    # Loop until valid choice is entered
    while my_choice not in valid_choices:

        if my_choice is not None:
            clear_screen()
            print()
            prompt(f"{repr(my_choice)} is not a valid choice!")
            print("\n" * 4)

        # Display available options
        prompt(f'Choose one:\n{"\n".join(display_choices)}')

        my_choice = input().lower()

        # Convert shorthand input to full key (e.g., "r" → "rock")
        for key in valid_choices:
            if my_choice in game_choices[key]["input"]:
                my_choice = key

    return my_choice


# Randomly select computer choice
def get_computer_choice(valid_choices):
    return random.choice(list(valid_choices))


# Display result of a single match and determine winner
def display_match_winner(player_choice, computer_choice, game_choices):

    print()
    prompt(
        f"You chose {player_choice.capitalize()}, "
        f"computer chose {computer_choice.capitalize()}\n"
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
        prompt("It's a tie!")
        print("\n")
        winner = "tie"

    return winner


# Plays a single round
def play_round(game_choices, valid_choices, display_choices):
    player = get_player_choice(game_choices, valid_choices, display_choices)
    clear_screen()
    computer = get_computer_choice(valid_choices)
    winner = display_match_winner(player, computer, game_choices)
    return winner


# Main game loop
def play_game(game_choices, valid_choices, display_choices,
              player_name="Human", computer_name="Computer"):
    max_matches_to_play = select_game_duration()
    clear_screen()

    print()
    prompt(f"{(', '.join(valid_choices)).title()}\n")
    prompt(f"{player_name} VS {computer_name}")
    prompt(
        f"{max_matches_to_play if max_matches_to_play > 0 else 'Unlimited'} "
        f"{make_plural('Match', max_matches_to_play)}\n"
    )

    played_matches = 0
    scores = {"player": 0, "computer": 0, "tie": 0}

    # Game loop
    while True:

        # Finite matches mode
        if max_matches_to_play != 0:
            while played_matches < max_matches_to_play:
                prompt(f"Match {played_matches + 1} of {max_matches_to_play}")
                game_winner = play_round(game_choices,
                                         valid_choices,
                                         display_choices
                                    )
                scores[game_winner] += 1
                played_matches += 1

        # Unlimited mode
        else:
            while True:
                prompt(f"Match {played_matches + 1}")
                game_winner = play_round(
                                game_choices,
                                valid_choices,
                                display_choices
                                )
                scores[game_winner] += 1
                played_matches += 1

                # Ask to continue
                if not play_again(
                    f"{player_name}, do you want to play again [y/n]? "
                    ):
                    clear_screen()
                    break

        # Determine final winner
        if scores["player"] > scores["computer"]:
            prompt(f"You won {match_plural(scores['player'])} "
                   f"out of {played_matches}, "
                   f"{computer_name} won {display_only(scores['computer'])}")
            print()
            prompt(f"{player_name}, you are the final winner!\n")
            break

        if scores["computer"] > scores["player"]:
            prompt(f"{computer_name} won {match_plural(scores['computer'])} "
                   f"out of {played_matches}, "
                   f"You won {display_only(scores['player'])}")
            print()
            prompt(f"{computer_name} is the final winner!\n")
            break

        # Tie case
        prompt(f"You won {match_plural(scores['player'])} and "
               f"{computer_name} won {match_plural(scores['computer'])} "
               f"out of {played_matches}")
        prompt("It's a tie!\n")

        if not play_again(
            f"{player_name}, "
            "do you want to play an extra match to decide a winner [y/n]? "
            ):
            clear_screen()
            break

        # Extend match count by 1
        max_matches_to_play = played_matches + 1


# Entry point of the program
def main():
    player_name, computer_name = get_players_name()

    game_choices = select_game_version(player_name)
    valid_choices = list(game_choices.keys())
    display_choices = [game_choices[key]["display"] for key in valid_choices]

    play_game(game_choices, valid_choices, display_choices,
              player_name, computer_name)

    prompt("By!\n")


# Run program only if executed directly (not imported)
if __name__ == "__main__":
    main()
