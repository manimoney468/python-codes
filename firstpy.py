decimal_number = int(input("Enter the number: "))
if (decimal_number < 0) or (decimal_number >= 100):
    print("num is not in range")
    exit()


def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0" 

    binary_digits = []
    
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_digits.append(str(remainder))
        decimal_number //= 2
    
    binary_digits.reverse()
    return binary_digits

binary_representation = decimal_to_binary(decimal_number)

def ones_complement(binary_string):
    complemented_string = ""
    
    for char in binary_string[2:]: 
        if char == "0":
            complemented_string += "1"
        elif char == "1":
            complemented_string += "0"
       
    return complemented_string

one_string = ones_complement(binary_representation)

def binary_to_decimal(binary_string):
    decimal_number = 0
    power = 0
    
    for digit in binary_string[::-1]:
        if digit == "1":
            decimal_number += 2 ** power
        power += 1
    
    return decimal_number

dec_num_ones = binary_to_decimal(one_string)
print("Decimal equivalent of one's complement:", dec_num_ones)
