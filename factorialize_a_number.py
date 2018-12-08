def factorialize(num):
    """Return the factorial of the provided integer"""
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i

    return factorial


print(factorialize(5))