"""
Type C: 2 registers type
Opcode
(5 bits)

Unused
(5 bits)

reg1
(3 bits)

reg2
(3 bits)
"""


"""
00011 - Move Register

Move content of reg2 into reg1.

mov reg1 reg2     
"""

"""
00111 - Divide 

Performs reg3/reg4. Stores the quotient in R0 and the remainder in R1. If reg4 is 0 then overflow flag is set and content of R0 and R1 are set to 0

div reg3 reg4
"""


"""
01101 - Invert 

Performs bitwise NOT of reg2. Stores the result in reg1.

not reg1 reg2
"""


"""
01110 - Compare 

Compares reg1 and reg2 and sets up the FLAGS register.

cmp reg1 reg2
"""

def mov(reg1, reg2):
    answer = "00011 00000 "
    match reg1:
        case R0:
            regsiter_string_1 = "000 "
        case R1:
            regsiter_string_1 = "001 "
        case R2:
            regsiter_string_1 = "010 "
        case R3:
            regsiter_string_1 = "011 "
        case R4:
            regsiter_string_1 = "100 "
        case R5:
            regsiter_string_1 = "101 "
        case R6:
            regsiter_string_1 = "110 "

    match reg2:
        case R0:
            regsiter_string_2 = "000"
        case R1:
            regsiter_string_2 = "001"
        case R2:
            regsiter_string_2 = "010"
        case R3:
            regsiter_string_2 = "011"
        case R4:
            regsiter_string_2 = "100"
        case R5:
            regsiter_string_2 = "101"
        case R6:
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)


def div(reg3, reg4):
    answer = "00111 00000 "
    match reg1:
        case R0:
            regsiter_string_1 = "000 "
        case R1:
            regsiter_string_1 = "001 "
        case R2:
            regsiter_string_1 = "010 "
        case R3:
            regsiter_string_1 = "011 "
        case R4:
            regsiter_string_1 = "100 "
        case R5:
            regsiter_string_1 = "101 "
        case R6:
            regsiter_string_1 = "110 "

    match reg2:
        case R0:
            regsiter_string_2 = "000"
        case R1:
            regsiter_string_2 = "001"
        case R2:
            regsiter_string_2 = "010"
        case R3:
            regsiter_string_2 = "011"
        case R4:
            regsiter_string_2 = "100"
        case R5:
            regsiter_string_2 = "101"
        case R6:
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)

    
def inv(reg 1, reg2):
    answer = "01101 00000 "
    match reg1:
        case R0:
            regsiter_string_1 = "000 "
        case R1:
            regsiter_string_1 = "001 "
        case R2:
            regsiter_string_1 = "010 "
        case R3:
            regsiter_string_1 = "011 "
        case R4:
            regsiter_string_1 = "100 "
        case R5:
            regsiter_string_1 = "101 "
        case R6:
            regsiter_string_1 = "110 "

    match reg2:
        case R0:
            regsiter_string_2 = "000"
        case R1:
            regsiter_string_2 = "001"
        case R2:
            regsiter_string_2 = "010"
        case R3:
            regsiter_string_2 = "011"
        case R4:
            regsiter_string_2 = "100"
        case R5:
            regsiter_string_2 = "101"
        case R6:
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)


def cmp(reg1, reg2):
    answer = "01110 00000 "
    match reg1:
        case R0:
            regsiter_string_1 = "000 "
        case R1:
            regsiter_string_1 = "001 "
        case R2:
            regsiter_string_1 = "010 "
        case R3:
            regsiter_string_1 = "011 "
        case R4:
            regsiter_string_1 = "100 "
        case R5:
            regsiter_string_1 = "101 "
        case R6:
            regsiter_string_1 = "110 "

    match reg2:
        case R0:
            regsiter_string_2 = "000"
        case R1:
            regsiter_string_2 = "001"
        case R2:
            regsiter_string_2 = "010"
        case R3:
            regsiter_string_2 = "011"
        case R4:
            regsiter_string_2 = "100"
        case R5:
            regsiter_string_2 = "101"
        case R6:
            regsiter_string_2 = "110"

    answer = answer + regsiter_string_1 + regsiter_string_2

    print(answer)
