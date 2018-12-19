def sum_all(arr):
    """
    Return the sum of two numbers and all the numbers between them.
    The lowest number will not always come first.
    """
    arr.sort()

    return sum(range(arr[0], arr[1] + 1))

# print(sum_all([1, 4]))


def diff_array(arr1, arr2):
    """Return the difference between two arrays in the form of an array."""
    new_arr = []

    [new_arr.append(item) for item in arr1 if item not in arr2]
    [new_arr.append(item) for item in arr2 if item not in arr1]

    return new_arr

# print(diff_array([1, 2, 3, 5], [1, 2, 3, 4, 5]))


def destroyer(arr, *args):
    """Remove all elements from arr that are given in args."""
    return [item for item in arr if item not in args]

# print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))


def what_is_in_a_name(collection, source):
    """
    Make a function that looks through an array of objects and returns 
    an array of all objects that have matching name and value pairs.
    """
    arr = []

    for dictionary in collection:
        for key in dictionary.keys():
            if key in source.keys():
                if dictionary[key] == source[key]:
                    arr.append(dictionary)

    return arr

# print(what_is_in_a_name(
#         [{'first': 'Romeo', 'last': 'Montague'},
#          {'first': 'Mercutio', 'last': None},
#          {'first': 'Tybalt', 'last': 'Capulet'}],
#         {'last': 'Capulet'}))


def spinal_case(string):
    """
    Convert a string to spinal case.
    Spinal case is all-lowercase-words-joined-by-dashes.
    """
    new_string = ''

    for char in string:
        if char == '_' or char == '-':
            new_string += ' '
        elif char == char.upper():
            new_string += ' ' + char
        else:
            new_string += char

    return '-'.join(new_string.lower().split())

# print(spinal_case("This Is Spinal Tap")


def translate_pig_latin(string):
    """Translate the provided string to pig latin."""
    for char in string:
        if char in 'aeiou':
            i = string.index(char)

            if i == 0:
                return string + 'way'
            else:
                return string[i:] + string[:i] + 'ay'

# print(translate_pig_latin('consonant'))


def my_replace(string, before, after):
    """
    Perform a search and replace on the sentence using the arguments provided 
    and return the new sentence. Preserve the case of the first character
    in the original word when you are replacing it.
    """
    array = string.split()

    if before == before.title():
        after = after.title()

    new_array = [after if word == before else word for word in array]
    new_sentence = ' '.join(new_array)

    return new_sentence

# print(my_replace("A quick brown fox jumped over the lazy dog", 'jumped', 'leaped'))


def pair_element(string):
    """
    Take each character, get its pair, and return the results as a 2d array.
    For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]
    """
    array_of_pairs = []
    base_pairs = {
        'A': ['A', 'T'],
        'T': ['T', 'A'],
        'C': ['C', 'G'],
        'G': ['G', 'C']}

    [array_of_pairs.append(base_pairs[char]) for char in string]
    
    return array_of_pairs

# print(pair_element('GCG'))


def fear_not_letter(string):
    """Find the missing letter in the passed letter range and return it."""
    array_of_char_codes = [ord(char) for char in string]

    for char_code in array_of_char_codes:
        if char_code == array_of_char_codes[-1]:
            return None

        next_index = array_of_char_codes.index(char_code) + 1
        next_char_code = array_of_char_codes[next_index]

        if next_char_code - char_code != 1:
            missing_letter = chr(char_code + 1)
            
            return missing_letter

# print(fear_not_letter('abce'))


def unite_unique(*arrays):
    """
    Take two or more arrays and return a new array of unique values in
    the order of the original provided arrays.
    """
    unique_items = []

    for array in arrays:
        for item in array:
            if item not in unique_items:
                unique_items.append(item)

    return unique_items

# print(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]))