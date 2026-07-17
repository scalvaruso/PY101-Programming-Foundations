import json


def select_language(messages):
    """
    Displays available languages and prompts the user to select one.
    Ensures the input matches one of the available language codes.
    """
    languages = list(messages.keys())   # Will store valid language codes (e.g. "en", "it", "el")
    selected_language = ""

    # Determine the longest language name to align output nicely
    max_len = max(len(data["name"]) for data in messages.values())

    # Keep asking until the user selects a valid language code
    while selected_language not in languages:
        for code, data in messages.items():
            # Print language name left-aligned, followed by its code
            print(f"{data['name']:<{max_len}} ==> {code}")
        # Read user input, remove extra spaces, and normalize to lowercase
        selected_language = input("==> ").strip().lower()
    
    return selected_language


def prompt(message):
    """
    Standardizes how messages are displayed to the user.
    Adds a prefix for consistency in the UI.
    """
    print(f"==> {message}")


def invalid_number(number_str):
    """
    Checks whether the provided string can be converted to a number.
    Returns True if invalid, False if valid.
    """
    try:
        # Attempt conversion to float (supports decimals)
        # Use int(number_str) instead if only integers are desired
        float(number_str)
    except ValueError:
        return True  # Conversion failed → invalid number

    return False  # Conversion succeeded → valid number


def main():
    """
    Main program flow:
    - Load messages from JSON
    - Let user choose a language
    - Run calculator loop until user exits
    """
    # Load language/messages configuration from JSON file
    with open("calculator_messages.json", "r") as file:
        messages = json.load(file)
    
    # Ask user to select a language
    lang = select_language(messages) 
    msgs = messages[lang]["messages"]  # Shortcut to selected language messages

    # Display welcome message
    prompt(msgs["welcome"])

    # Main calculator loop
    while True:
        # Run a complete calculator operation and store the returned result
        result = operation(msgs)

        # If the operation was successful, display the calculated value
        if isinstance(result, (int, float)):
            prompt(f"{msgs['result']} {result}")
        else:
            # If division by zero occurred, display the appropriate error message
            # using the message key returned by the operation function
            prompt(msgs[result])

        # Ask user if they want another calculation
        prompt(msgs["another_operation"])
        answer = input()

        # Accept both language-specific "yes" and English "y"
        # If input does not match, exit loop
        if answer and answer[0].lower() not in (msgs["answer"], "y"):
            break
    
    # Goodbye message when exiting
    prompt(msgs["goodbye"])


def operation(msgs):
    """
    Handles a single calculator operation:
    - Prompts for two numbers
    - Validates input
    - Prompts for operation type
    - Returns computed result
    """

    # Get first number
    prompt(msgs["prompt_first_number"])
    number1 = input()

    # Validate input until a valid number is entered
    while invalid_number(number1):
        prompt(msgs["invalid_number"])
        number1 = input()

    # Get second number
    prompt(msgs["prompt_second_number"])
    number2 = input()

    # Validate input again
    while invalid_number(number2):
        prompt(msgs["invalid_number"])
        number2 = input()

    # Ask user which operation to perform
    prompt(msgs["prompt_operation"])
    operation = input()

    # Ensure operation is one of the allowed options
    while operation not in ["1", "2", "3", "4"]:
        prompt(msgs["invalid_operation"])
        operation = input()

    # Perform the selected operation
    match operation:
        case "1":  # Addition
            output = float(number1) + float(number2)
        case "2":  # Subtraction
            output = float(number1) - float(number2)
        case "3":  # Multiplication
            output = float(number1) * float(number2)
        case "4":  # Division
            # Check that the divisor is not zero before performing the calculation
            if float(number2) != 0:
                output = float(number1) / float(number2)
            else:
                # Return a message key instead of a result so the caller
                # can display the correct translated error message
                return "zero_division"

    return output    


# Entry point of the program
main()