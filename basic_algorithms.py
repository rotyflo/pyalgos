def convert_to_f(celsius):
    """Convert celsius into fahrenheit"""
    return celsius * 9 / 5 + 32


def reverse_string(string):
    """Reverse the provided string"""
    return ''.join(reversed(list(string)))


def factorialize(num):
    """Return the factorial of the provided integer"""
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i

    return factorial


def find_longest_word_length(string):
    """Return the length of the longest word in the provided sentence"""
    list_of_words = string.split(' ')

    longest = 0

    for word in list_of_words:
        if len(word) > longest:
            longest = len(word)

    return longest


def largest_of_four(array):
    """Return an array consisting of the largest
       number from each provided sub-array"""
    largest_of_each = []

    for sub_array in array:
        largest_number = 0

        for number in sub_array:
            if number > largest_number:
                largest_number = number

        largest_of_each.append(largest_number)

    return largest_of_each


def confirm_ending(string, target):
    """Check if a string (first arg) ends with the given target string"""
    return target == string[-len(target):]


def repeat_string_num_times(string, num):
    """Repeat a given string for num times.
       Return an empty string if num is not a positive number."""
    return string * num


def truncate_string(string, num):
    """Truncate a string if it is longer than the given maximum string length. 
       Return the truncated string with a ... ending."""
    if len(string) > num:
        return string[:num] + "..."
    else:
        return string 