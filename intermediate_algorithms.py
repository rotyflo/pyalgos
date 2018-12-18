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
    arr = [item for item in arr if item not in args]

    return arr

print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))