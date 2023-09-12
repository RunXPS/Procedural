#################################################
#  Author: Ryan Krasinski
#  Date: 9/13/2021
#  medium_functions.py
#################################################
from runTests import run_test, run_test_float, close_enough
###################FREE CODE######################################
def is_leap(year):
    """prec:  year is a modern year
postc: returns True if the year leaps.
"""
    out = False
    if year %4 == 0:
        out = not out
        if year % 100 == 0:
            out = not out
            if year % 400 == 0:
                out = not out
    return out
##############END FREE CODE######################################


###################Problem 1################
def meanie(theList):
    """Precondition: theList is a non-empty list of numbers
Postcondition: return the mean of the numbers."""
    return sum(theList)/len(theList)
###################Problem 2################
# 1 is January, 2 is February, etc.
def day_in_year(year, month, day):
    """prec:  year/month/day is a valid date
    postc: returns the ordinal position of the day in the year
    (Feb 15 is the 46th day of year 2000).
    Hint:  The built-in function sum is your friend. Learn about it."""

    lengths = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(lengths[:month-1])+day
###################Problem 3################
def days_left_in_year(year, month, day):
    """prec:  year/month/day is a valid date
    postc: returns the number of days left in the year
    (Feb 15 is the 44th day of year 2000)."""
    if is_leap(year) == True:
        return 366 - day_in_year(year, month, day)
    else:
        return 365 - day_in_year(year, month, day)
###################Problem 4################
def days_to_graduation(year, month, day):
    """prec:  year/month/ is a valid date before graduation
    in 2020 or 2021.  It's 29 May 2021.
    postc: returns the number of days until graduation 
    If the year is illegal, or if a date after 29 May 2021 is entered,
    return "ILLEGAL INPUT"  """
    if year == 2020:
        return (514 - day_in_year(year, month, day))
    elif year == 2021:
        return (149 - day_in_year(year, month, day))
    elif year < 2020 or year > 2021:
        return "ILLEGAL INPUT"
###################Problem 5################
def dhms(secs):
    """prec:  secs is a nonnegative integer
    postc: return a STRING of the form d:hh:mm:ss, where d is the number
    of days, h is the number of hours, m is the number     of minutes, and
    s is the number of seconds, h < 24, 0 <= m, s, < 60.  Give each of
    h, m, s a two character width, padding with zeroes as needed.  """
    mins = secs//60
    secs = secs%60
    hours = mins//60
    mins = mins%60
    days = hours//24
    hours = hours%24

    if secs < 10:
        secs = "0" + str(secs)
    if mins < 10:
        mins = "0" + str(mins)
    if hours < 10:
        hours = "0" + str(hours)
    return f"{days}:{hours}:{mins}:{secs}"
###################Problem 6################
def water_closet(theString):
    """precondition: theString is a string.
postcondition: returns a tuple (c, w, l) where c is the number of
characters in theString, w is the number of words, and l is the number of
lines in the string"""
    
    words = len(theString.split(" "))
    lines = theString.count("\n")+1
    if lines < 1:
        lines = 1
    if len(theString.split(" ")) <= 1:
        if len(theString.split("\n")) <= 1:
            words = 0
        else:
            words = len(theString.split("\n"))
    return tuple([len(theString), len(theString.split()), lines])
###################Problem 7################
def math_case(x):
    """precondition: x is a number
postcondition: If x > 4, f(x) = x - 4, if x < -5, f(x) = x + 5,
otherwise, f(x) = 0."""
    if x > 4:
        return x - 4
    elif x < -5:
        return x + 5
    else:
        x = 0
    return x

def main():
    print("###################Problem 1################")
    test = [[1,2,3,4,5,6]]
    expected = 3.5
    run_test(meanie, expected, test)
    test = [[-3, -2, 0, 0, 6, 5]]
    expected = 1.0
    run_test(meanie, expected, test)
    print("###################Problem 2################")
    test = [2020, 1, 25]
    expected = 25
    run_test(day_in_year, expected, test)
    test = [2024, 6, 4]
    expected = 156
    run_test(day_in_year, expected, test)
    test = [2021, 6, 4]
    expected = 155
    run_test(day_in_year, expected, test)
    print("###################Problem 3################")
    test = [2020, 1, 25]
    expected = 341
    run_test(days_left_in_year, expected, test)
    test = [2024, 6, 4]
    expected = 210
    run_test(days_left_in_year, expected, test)
    test = [2021, 6, 4]
    expected = 210
    run_test(days_left_in_year, expected, test)
    print("###################Problem 4################")
    test = [2020, 1, 1]
    expected = 365+148
    expected = 513
    run_test(days_to_graduation, expected, test)
    test = [2024, 6, 4]
    expected = "ILLEGAL INPUT"
    run_test(days_to_graduation, expected, test)
    test = [2021, 5, 28]
    expected = 1
    run_test(days_to_graduation, expected, test)
    print("###################Problem 5################")
    test = [1]
    expected = "0:00:00:01"
    run_test(dhms, expected, test)
    test = [86461]
    expected = "1:00:01:01"
    run_test(dhms, expected, test)
    print("###################Problem 6################")
    test = ["I\nLike\nCows"]
    expected = tuple([11, 3, 3])
    run_test(water_closet, expected, test)
    test = ["I Like Cows"]
    expected = tuple([11, 3, 1])
    run_test(water_closet, expected, test)
    test = ["I  Like  Cows"]
    expected = tuple([13, 3, 1])
    run_test(water_closet, expected, test)
    test = ["I"]
    expected = tuple([1, 1, 1])
    run_test(water_closet, expected, test)
    test = ["         "]
    expected = tuple([9, 0, 1])
    run_test(water_closet, expected, test)
    print("###################Problem 7################")
    test = [4]
    expected = 0
    run_test(math_case, expected, test)
    test = [-10]
    expected = -5
    run_test(math_case, expected, test)
    test = [10]
    expected = 6
    run_test(math_case, expected, test)
main()