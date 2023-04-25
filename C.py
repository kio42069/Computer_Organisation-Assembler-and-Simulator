def mov(reg1, reg2):
    answer = "0001100000"
    match reg1:
        case "R0":
            regsiter_string_1 = "000"
        case "R1":
            regsiter_string_1 = "001"
        case "R2":
            regsiter_string_1 = "010"
        case "R3":
            regsiter_string_1 = "011"
        case "R4":
            regsiter_string_1 = "100"
        case "R5":
            regsiter_string_1 = "101"
        case "R6":
            regsiter_string_1 = "110"

    match reg2:
        case "R0":
            regsiter_string_2 = "000"
        case "R1":
            regsiter_string_2 = "001"
        case "R2":
            regsiter_string_2 = "010"
        case "R3":
            regsiter_string_2 = "011"
        case "R4":
            regsiter_string_2 = "100"
        case "R5":
            regsiter_string_2 = "101"
        case "R6":
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)


def div(reg1, reg2):
    answer = "0011100000"
    match reg1:
        case "R0":
            regsiter_string_1 = "000"
        case "R1":
            regsiter_string_1 = "001"
        case "R2":
            regsiter_string_1 = "010"
        case "R3":
            regsiter_string_1 = "011"
        case "R4":
            regsiter_string_1 = "100"
        case "R5":
            regsiter_string_1 = "101"
        case "R6":
            regsiter_string_1 = "110"

    match reg2:
        case "R0":
            regsiter_string_2 = "000"
        case "R1":
            regsiter_string_2 = "001"
        case "R2":
            regsiter_string_2 = "010"
        case "R3":
            regsiter_string_2 = "011"
        case "R4":
            regsiter_string_2 = "100"
        case "R5":
            regsiter_string_2 = "101"
        case "R6":
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)

    
def inv(reg1, reg2):
    answer = "0110100000"
    match reg1:
        case "R0":
            regsiter_string_1 = "000"
        case "R1":
            regsiter_string_1 = "001"
        case "R2":
            regsiter_string_1 = "010"
        case "R3":
            regsiter_string_1 = "011"
        case "R4":
            regsiter_string_1 = "100"
        case "R5":
            regsiter_string_1 = "101"
        case "R6":
            regsiter_string_1 = "110"

    match reg2:
        case "R0":
            regsiter_string_2 = "000"
        case "R1":
            regsiter_string_2 = "001"
        case "R2":
            regsiter_string_2 = "010"
        case "R3":
            regsiter_string_2 = "011"
        case "R4":
            regsiter_string_2 = "100"
        case "R5":
            regsiter_string_2 = "101"
        case "R6":
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)


def cmp(reg1, reg2):
    answer = "0111000000"
    match reg1:
        case "R0":
            regsiter_string_1 = "000"
        case "R1":
            regsiter_string_1 = "001"
        case "R2":
            regsiter_string_1 = "010"
        case "R3":
            regsiter_string_1 = "011"
        case "R4":
            regsiter_string_1 = "100"
        case "R5":
            regsiter_string_1 = "101"
        case "R6":
            regsiter_string_1 = "110"

    match reg2:
        case "R0":
            regsiter_string_2 = "000"
        case "R1":
            regsiter_string_2 = "001"
        case "R2":
            regsiter_string_2 = "010"
        case "R3":
            regsiter_string_2 = "011"
        case "R4":
            regsiter_string_2 = "100"
        case "R5":
            regsiter_string_2 = "101"
        case "R6":
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)

mov("R0", "R1")
div("R0", "R1")
inv("R0", "R1")
cmp("R0", "R1")