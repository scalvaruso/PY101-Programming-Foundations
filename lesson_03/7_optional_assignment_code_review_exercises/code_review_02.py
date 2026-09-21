# Vlad's Solution

def is_leap_year(year):
    is_a_leap_year = False
    if year % 4 == 0:
        is_a_leap_year = True
    if year % 100 == 0:
     is_a_leap_year = False
    if year % 400 == 0:
            is_a_leap_year = True
    return is_a_leap_year