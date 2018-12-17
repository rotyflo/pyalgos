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