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


def convert_html(string):
    """
    Convert the characters &, <, >, " (double quote), and ' (apostrophe),
    in a string to their corresponding HTML entities.
    """
    html_entities = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&apos;'}
    new_string = ""

    for char in string:
        if char in html_entities.keys():
            new_string += html_entities[char]
        else:
            new_string += char

    return new_string

# print(convert_html("Dolce & Gabbana"))


def sum_odd_fibs(num):
    """
    Return the sum of all odd Fibonacci numbers
    that are less than or equal to num.
    """
    fib_nums = [1]
    fib = 1

    while fib <= num:
        fib_nums.append(fib)

        last_num = fib_nums[-1]
        second_last_num = fib_nums[-2]
        fib = last_num + second_last_num

    summed_odds = sum([fib for fib in fib_nums if fib % 2 == 1])

    return summed_odds

# print(sum_odd_fibs(4))


def sum_primes(num):
    """Sum all the prime numbers up to and including the provided number."""
    prime_numbers = []

    for numerator in range(2, num + 1):
        is_prime = True

        for denominator in range(2, numerator):
            if numerator % denominator == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(numerator)

    return sum(prime_numbers)

# print(sum_primes(977))


def smallest_common(arr):
    """
    Find the smallest common multiple of the provided parameters that can be
    evenly divided by both, as well as by all sequential numbers in the range
    between these parameters.
    """
    arr.sort()
    first = arr[0]
    last = arr[1] + 1
    multiple = 0
    found = False

    while not found:
        found = True
        multiple += 1

        for num in range(first, last):
            if multiple % num != 0:
                found = False

    return multiple

# print(smallest_common([5, 1]))


def drop_elements(array, func):
    """
    Iterate through array and remove each element until func returns true when
    the iterated element is passed through it.
    """
    filtered_array = [item for item in array if func(item)]

    return filtered_array

# print(drop_elements([1, 2, 3], lambda n: n < 3))


def steamroll_array(array):
    """
    Flatten a nested array. You must account for varying levels of nesting.
    """
    flat_str = str(array).replace('[', '').replace(']', '').replace(' ,', '')
    flat_arr = eval('[' + flat_str + ']')

    return flat_arr

# print(steamroll_array([1, [2], [3, [[4]]]]))


def binary_agent(string):
    """
    Return an English translated sentence of the passed binary string.
    The binary string will be space separated.
    """
    binary = string.split()
    decoded_string = ''

    for byte in binary:
        bit_value = 128
        byte_value = 0

        for bit in byte:
            if bit == '1':
                byte_value += bit_value

            bit_value /= 2

        character = chr(int(byte_value))
        decoded_string += character

    return decoded_string

# print(binary_agent("01000001 01110010 01100101 01101110 00100111 01110100 "
#     "00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 "
#     "01110011 00100000 01100110 01110101 01101110 00100001 00111111"))


def truth_check(collection, pre):
    """Check if 'pre' is truthy on all the elements of 'collection'."""
    for dictionary in collection:
        if pre not in dictionary.keys():
            return False

        if not dictionary[pre]:
            return False

    return True

# print(truth_check(
#     [{"user": "Tinky-Winky", "sex": "male"},
#      {"user": "Dipsy", "sex": "male"},
#      {"user": "Laa-Laa", "sex": "female"},
#      {"user": "Po", "sex": "female"}],
#     "sex"))


def add_together(*args):
    """
    Sums two arguments together. If only one argument is provided,
    then return a function that expects one argument and returns the sum.
    """
    if len(args) == 1:
        return lambda x: args[0] + x
    else:
        return args[0] + args[1]

# sum_two_and = add_together(2)

# print(sum_two_and(3))


class Person():
    """
    Build a class with the following methods:
    get_first_name()
    get_last_name()
    get_full_name()
    set_first_name(first)
    set_last_name(last)
    set_full_name(full)
    """

    def __init__(self, first_name, last_name):
        """Initialize values for person"""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name

    def get_first_name(self):
        """Get first name of person."""
        return self.first_name.title()

    def get_last_name(self):
        """Get last name of person."""
        return self.last_name.title()

    def get_full_name(self):
        """Get full name of person."""
        return self.full_name.title()

    def set_first_name(self, first):
        """Set first name of person."""
        self.first_name = first
        self.full_name = self.first_name + ' ' + self.last_name

    def set_last_name(self, last):
        """Set last name of person."""
        self.last_name = last
        self.full_name = self.first_name + ' ' + self.last_name

    def set_full_name(self, full):
        """Set full name of person."""
        self.full_name = full

        names = full.split()

        self.first_name = names[0]
        self.last_name = names[-1]

# bob = Person('bob', 'ross')

# print(bob.get_full_name())

# bob.set_first_name('robert')

# print(bob.get_full_name())

# bob.set_full_name('robert tyler flores')

# print(bob.get_first_name())
# print(bob.get_last_name())
# print(bob.get_full_name())