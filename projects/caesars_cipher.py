def rot13(string):
    """
    Decode a ROT13 encoded string. All letters will be uppercase.
    Do not transform any non-alphabetic character, but do pass them on.
    """
    decoded_string = ''

    for char in string:
        char_code = ord(char)

        if char_code in range(65, 91):
            if char_code < 78:
                rot13_char = chr(char_code + 13)
            else:
                rot13_char = chr(char_code - 13)
        else:
            rot13_char = char

        decoded_string += rot13_char

    return decoded_string

# print(rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT."))