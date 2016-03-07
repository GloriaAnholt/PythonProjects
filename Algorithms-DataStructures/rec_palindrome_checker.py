# Algorithms and Data Structures: Recursion
# 03.07.2016
# @totallygloria


def palindrome_checker(s):
    # Write a function that takes a string as a parameter and returns True if
    # the string is a palindrome, False otherwise.

    stripped = s.translate(None, " !,.?'\":;-~`@#$%^&*()_+={}[]<>/|\\")

    if len(stripped) <= 1:
        return True
    else:
        if stripped[0] == stripped[-1]:
            return palindrome_checker(stripped[1:len(stripped) - 1])
        else:
            return False