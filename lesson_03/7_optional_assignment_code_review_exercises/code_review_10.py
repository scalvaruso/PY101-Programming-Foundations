"""
Write a function that takes a question as a string argument. The function should:

    Display the string passed as an argument.
    Get the user's input as a string.
    If the input is y or yes:
        Print Here we go again!
        Go back to where the function was called.
    If the input is n or no:
        Print Okay. See you later.
        Go back to where the function was called.
    If the input is not one of the expected answers:
        Print You goofed! That is not a valid answer.
        Go back to step 1.

Additional Rules

    The function should work with both uppercase and lowercase inputs, as well as mixed case.
    The function should strip any leading or trailing whitespace from the input before checking its value.
"""

# Staff Solution
"""
def yes_no_response(question):
    while True:
        print(question)
        answer = input().lower().strip()

        if answer in ['y', 'yes']:
            print('Here we go again!')
            return
        elif answer in ['n', 'no']:
            print('Okay. See you later.')
            return
        else:
            print('You goofed! That is not a valid answer.')
"""
"""
The yes_no_response function takes a string argument that is in the form of a question.
The main part of this code is relatively straightforward. We need to print the question, then obtain some input from the user. Since the additional rules state that the input is case sensitive, we covert the input to lowercase then strip any leading or whitespace from the input before we assign it to the answer variable. The code input().lower().strip() first retrieves the input, converts the result to lowercase, then strips the whitespace.
Next, we check whether the answer is one of the four allowed choices. First, we check for an answer that matches one of the two strings y or yes, then we check whether it matches n or no. Note that we use the in operator to determine whether the user's input is one of the expected answers. Depending on which answer is given, we display an appropriate message then exit from the function.
If the input isn't valid, we display an error message then repeat the entire process again. The tricky part involves how to implement that repetition. To do that, we put all our code inside a while True: loop; Python will repeat the block of the loop until a break or return statement is executed.
"""

# Leigh's Solution

def yes_no_response(question):
    while True:
        print(question)
        answer = input()

        if answer == 'y' or answer == 'yes':
            print('Here we go again!')
            return
        elif answer == 'n' or answer == 'no':
            print('Okay. See you later.')
            return
        else:
            print('You goofed! That is not a valid answer.')


yes_no_response("Do you want to continue? (y/n)")
yes_no_response("Are you absolutely sure? (yes/no)")
print("All done.")