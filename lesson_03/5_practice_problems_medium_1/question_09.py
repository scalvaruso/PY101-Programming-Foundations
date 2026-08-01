# Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?

bar(foo())

# My Solution

# False

# Launch School Solution

# False

"""
When bar(foo()) is called, the foo function is executed first, returning "yes".
This return value ("yes") is then passed as the argument to the bar function.
In bar, the parameter param is now "yes".
The expression (param == "no") and (foo() or "no") is evaluated as follows:

    param == "no" evaluates to False since param is "yes".
    Due to the and operator, (foo() or "no") is not executed since the first part of the and expression is already False.
    Since the left side of the and is False, Python returns False.

"""
