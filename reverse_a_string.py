def reverse_string(string):
    array = list(string)
    array.reverse()
    reassembled_string = ''.join(array)
    
    return reassembled_string

string = input("Input: ")
reversed_string = reverse_string(string)

print("Reversed: " + reversed_string)