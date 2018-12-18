def sum_all(arr):
    """
    Return the sum of two numbers and all the numbers between them.
    The lowest number will not always come first.
    """
    arr.sort()

    smallest = arr[0]
    biggest = arr[1]
    total = sum(range(smallest, biggest + 1))

    return total

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