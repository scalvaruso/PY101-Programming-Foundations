# Louisa's Solution
def crunch(text):
    result = ''
    i = 0
    while i < len(text):
        if i < len(text) - 1:
            if text[i] != text[i + 1]:
                result += text[i]
        else:
            result += text[i]
        i += 1
    return result


# Staff Solution and Explanation
"""
def crunch(text):
    index = 0
    crunched_text = ''

    while index < len(text):
        if index == len(text) - 1 or text[index] != text[index + 1]:
            crunched_text += text[index]

        index += 1

    return crunched_text

Our solution builds a string named crunched_text by iterating over the characters in the text argument.
While iterating, we append the character at the current index to crunched_text if the character is not equal to the next character. If it is equal, then do nothing.

NOTE that we also need to determine whether we are dealing with the last character in the original string.
"""


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')