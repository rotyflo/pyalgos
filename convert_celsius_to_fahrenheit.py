def convert_to_f(c):
    return float(c) * 9 / 5 + 32

celsius = input("Celsius: ")
fahrenheit = convert_to_f(celsius)

print("Fahrenheit: " + str(fahrenheit))