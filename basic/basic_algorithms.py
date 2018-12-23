def convert_to_f(celsius):
    """Convert celsius into fahrenheit"""
    return celsius * 9 / 5 + 32

# print(convert_to_f(30))


def reverse_string(string):
    """Reverse the provided string"""
    return ''.join(reversed(list(string)))

# print(reverse_string("hello"))


def factorialize(num):
    """Return the factorial of the provided integer"""
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i

    return factorial

# print(factorialize(5))


def find_longest_word_length(string):
    """Return the length of the longest word in the provided sentence"""
    list_of_words = string.split(' ')

    longest = 0

    for word in list_of_words:
        if len(word) > longest:
            longest = len(word)

    return longest

# print(find_longest_word_length("The quick brown fox jumped over the lazy dog"))


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

# print(largest_of_four([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]))


def confirm_ending(string, target):
    """Check if a string (first arg) ends with the given target string"""
    return target == string[-len(target):]

# print(confirm_ending("Bastion", "n"))


def repeat_string_num_times(string, num):
    """Repeat a given string for num times.
       Return an empty string if num is not a positive number."""
    return string * num

# print(repeat_string_num_times("abc", 3))


def truncate_string(string, num):
    """Truncate a string if it is longer than the given maximum string length. 
       Return the truncated string with a ... ending."""
    if len(string) > num:
        return string[:num] + "..."
    else:
        return string

# print(truncated("A-tisket a-tasket A green and yellow basket", 8))


def find_element(array, func):
    """Look through an array and return the first element in the array that 
       passes a truth test. If no element passes the test, return undefined."""
    for num in array:
        if func(num) == True:
            return num

# print(find_element([1, 2, 3, 4], lambda num: num % 2 == 0))


def boo_who(boolean):
    """Check if a value is classified as a boolean primitive.
       Return true or false."""
    #Filter out (True == 1) and (False == 0)
    strict_true = boolean == True and type(boolean) == type(True)
    strict_false = boolean == False and type(boolean) == type(False)

    return strict_true or strict_false

# print(boo_who(None))


def title_case(string):
    """Return the provided string with the first letter of each word capitalized.
       Make sure the rest of the word is in lower case."""
    #Corrects (I'm) to (I'M) error caused by the title() method
    words = string.split()
    title_case_words = []
    
    [title_case_words.append(word[0].upper() + word[1:]) for word in words]

    return ' '.join(title_case_words)

# print(title_case("I'm a little tea pot"))


def franken_splice(arr1, arr2, n):
    """Insert arr1 at index n of arr2"""
    while arr1:
        arr2.insert(n, arr1.pop(0))
        n += 1

    return arr2

# print(franken_splice([1, 2, 3], [4, 5, 6], 1))


def bouncer(array):
    """Remove all falsy values from an array"""
    filtered_array = []

    for item in array:
        if item:
            filtered_array.append(item)

    return filtered_array

# print(bouncer([7, "ate", "", False, 9]))


def get_index_to_ins(array, num):
    """Return the lowest index at which num should be inserted into array
       once it has been sorted. The returned value should be a number."""
    for index in range(len(array)):
        if sorted(array)[index] >= num:
            return index

# print(get_index_to_ins([40, 60], 50))


def mutation(arr):
    """Return true if the string in the first element of the array contains all
       of the letters of the string in the second element of the array"""
    matching_letters = 0

    for letter_1 in arr[1]:
        for letter_0 in arr[0]:
            if letter_0.lower() == letter_1.lower():
                matching_letters += 1
                break

    return matching_letters == len(arr[1])

# print(mutation(["hello", "hey"]))


def chunk_array_in_groups(arr, size):
    """Split an array into groups the length of size and returns
       them as a two-dimensional array"""
    group_of_arrays = []

    while arr:
        new_array = []

        for num in range(size):
            if arr:
                new_array.append(arr.pop(0))
            else:
                break

        group_of_arrays.append(new_array)

    return group_of_arrays

# print(chunk_array_in_groups(["a", "b", "c", "d"], 2))