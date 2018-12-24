def convert_to_roman(num):
    """Convert the given number into a roman numeral."""
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'}
    converted_number = ''

    for val in roman_numerals:
        while num >= val:
                num -= val
                converted_number += roman_numerals[val]

    return converted_number

# print(convert_to_roman(3999))