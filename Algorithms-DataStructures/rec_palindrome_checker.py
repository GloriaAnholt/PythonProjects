def palindrome_checker(s):
    # Write a function that takes a string as a parameter and returns True if
    # the string is a palindrome, False otherwise.

    stripped = s.translate(None, " !,.?'\":;-~`@#$%^&*()_+={}[]<>/|\\")

    if len(stripped) <= 1:
        return True
    elif len(stripped) == 2 or len(stripped) == 3:
        return (stripped[0] == stripped[-1])
    else:
        #print (stripped[0], stripped[-1])
        if (stripped[0] == stripped[-1]):
            return palindrome_checker(stripped[1:len(stripped) - 1])

