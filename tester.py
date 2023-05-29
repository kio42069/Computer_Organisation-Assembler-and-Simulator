def binary_to_decimal(number):
    number = str(int(number))
    decimal = 0
    i = len(number)-1
    while(i >= 0):
        decimal += int(number[i])*(2**(len(number)-1-i))
        i -= 1
    return decimal
print(binary_to_decimal("10101"))