def factorialize(num):
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i

    return factorial

user_input = int(input("Give me a number: "))
factorial = factorialize(user_input)

print("Factorial: " + str(factorial))