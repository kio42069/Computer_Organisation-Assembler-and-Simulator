def decimal_to_binary(n):
    result = 0
    digits = 0
    
    while(n):
        result = (result*10) + (n%2)
        n //= 2
        digits += 1

    result = str(result)

    while (digits < 7):
        result = "0" + result
        digits += 1

    return result


n = int(input("n: "))
print(decimal_to_binary(n))