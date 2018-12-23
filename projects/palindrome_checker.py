def palidrome(string):
    """
    Remove all non-alphanumeric characters and turn everything into the same
    case in order to check for palindromes. Return true if the given string is
    a palindrome. Otherwise, return false.
    """
    alphanum = 'abcdefghijklmnopqrstuvwxyz0123456789'
    allowed_chars = [char for char in string.lower() if char in alphanum]

    clean_string = ''.join(allowed_chars)
    reversed_string = ''.join(reversed(allowed_chars))

    is_palindrome = clean_string == reversed_string

    return is_palindrome

# print(palidrome("A man, a plan, a canal. Panama"))