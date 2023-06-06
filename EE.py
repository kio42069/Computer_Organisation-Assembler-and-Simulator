#decimal to binary
def decimal_to_binary(number):
    return bin(int(number))[2:]

#binary to decimal
def binary_to_decimal(number):
    number = str(int(number))
    decimal = 0
    i = len(number)-1

    while(i >= 0):
        decimal += int(number[i])*(2**(len(number)-1-i))
        i -= 1

    return decimal


def A(curr_line, registers):
    opcode = curr_line[:5]
    reg1 = curr_line[7:10]
    reg2 = curr_line[10:13]
    reg3 = curr_line[13:16]
    value2 = binary_to_decimal(str(int(registers[reg2])))
    value3 = binary_to_decimal(str(int(registers[reg3])))

    match opcode:
        case "00000":
            add(value2, value3, reg1, registers)
        
        case "00001":
            sub(value2, value3, reg1, registers)

        case "00110":
            mul(value2, value3, reg1, registers)

        case "01010":
            xor(value2, value3, reg1, registers)
        
        case "01011":
            Or(value2, value3, reg1, registers)

        case "01100":
            And(value2, value3, reg1, registers)

    return registers

def B(curr_line, registers):
    opcode = curr_line[:5]
    reg = curr_line[6:9]
    imm = curr_line[9:16]

    match opcode:
        case "00010":
            mov_i(reg, imm, registers)

        case "01000":
            rs(reg, imm, registers)

        case "01001":
            ls(reg, imm, registers)

    return registers

def C(curr_line, registers):
    opcode = curr_line[:5]
    reg1 = curr_line[10:13]
    reg2 = curr_line[13:16]
    value2 = binary_to_decimal(str(int(registers[reg2])))

    match opcode:
        case "00011":
            mov_r(reg1, value2, registers)

        case "00111":
            div(reg1, value2, registers)

        case "01101":
            Not(reg1, value2, registers)

        case "01110":
            cmp(reg1, value2, registers)

    return registers

def D(curr_line, registers, memory):
    opcode = curr_line[:5]
    reg = curr_line[6:9]
    var = binary_to_decimal(curr_line[9:16])

    match opcode:
        case "00100":
            ld(reg, var, registers, memory)

        case "00101":
            st(reg, var, registers, memory)

    return registers

def E(curr_line, PC, registers):
    opcode = curr_line[:5]
    label = curr_line[9:16]
    label = binary_to_decimal(label)

    match opcode:
        case "01111":
            registers, PC = jmp(label, PC, registers)

        case "11100":
            registers, PC = jlt(label, PC, registers)

        case "11101":
            registers, PC = jgt(label, PC, registers)

        case "11111":
            registers, PC = je(label, PC, registers)

    return registers, PC

def add(value2, value3, reg1, registers):
    value1 = decimal_to_binary(str(int(value2) + int(value3)))

    if len(value1) > 16:
        registers[reg1] = "0000000000000000"
        registers["111"] = registers["111"][:12] + "1" + registers["111"][13:]

    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1

    return registers
    

def sub(value2, value3, reg1, registers):
    value1 = decimal_to_binary(str(int(value2) - int(value3)))

    if len(value1) > 16 or int(value2) < int(value3):
        registers[reg1] = "0000000000000000"
        registers["111"] = registers["111"][:12] + "1" + registers["111"][13:]

    else:
        num_zeroes = 16 - len(value1)

        for i in range(num_zeroes):
            value1 = '0' + value1

        registers[reg1] = value1

    return registers
    
def mov_i(reg, imm, registers):
    num_zeroes = 16-len(imm)
    imm = "0"*num_zeroes + imm
    registers[reg] = imm
    return registers


def mov_r(reg1, value2, registers):
    value1 = value2
    registers[reg1] = value1
    return registers

def ld(reg, var, registers, memory):
    registers[reg] = memory[int(var)]
    return registers

def st(reg, var, registers, memory):
    memory[int(var)] = registers[reg]
    return registers

def mul(value2, value3, reg1, registers):
    value1 = decimal_to_binary(str(int(value2) * int(value3)))

    if len(value1 > 16):
        registers[reg1] = "0000000000000000"
        registers["111"] = registers["111"][:12] + "1" + registers["111"][13:]

    else:
        num_zeroes = 16 - len(value1)

        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1

    return registers

def div(reg1, value2, registers):
    if value2 == 0:
        registers["000"] = "0000000000000000"
        registers["001"] = "0000000000000000"
        registers["111"] = registers["111"][:12] + "1" + registers["111"][13:]

    else:
        value1 = registers[reg1]
        quotient = value1 // value2
        remainder = value1 % value2
        registers["000"] = quotient
        registers["001"] = remainder

    return registers

def rs(reg, imm, registers):
    imm = int(binary_to_decimal(imm))
    value = int(binary_to_decimal(registers[reg]))
    registers[reg] = decimal_to_binary(str(value >> imm))

    return registers

def ls(reg, imm, registers):
    imm = int(binary_to_decimal(imm))
    value = int(binary_to_decimal(registers[reg]))
    registers[reg] = decimal_to_binary(str(value << imm))

    return registers


def xor(value2, value3, reg1, registers):
    value1 = decimal_to_binary(str(int(value2) ^ int(value3)))

    if len(value1) > 16:
        registers[reg1] = "0000000000000000"
        registers["111"] = registers["111"][:12] + "1" + registers["111"][13:]

    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1

    return registers

def Or(value2, value3, reg1, registers):
    value1 = decimal_to_binary(str(int(value2) | int(value3)))

    if len(value1) > 16:
        registers[reg1] = "0000000000000000"
        registers["111"] = registers["111"][:12] + "1" + registers["111"][13:]

    else:
        num_zeroes = 16 - len(value1)

        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1

    return registers

def And(value2, value3, reg1, registers):
    value1 = decimal_to_binary(str(int(value2) & int(value3)))

    if len(value1) > 16:
        registers[reg1] = "0000000000000000"
        registers["111"] = registers["111"][:12] + "1" + registers["111"][13:]

    else:
        num_zeroes = 16 - len(value1)

        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1

    return registers

def Not(reg1, value2, registers):
    value1 = decimal_to_binary(str(int(~value2)))
    registers[reg1] = value1

    return registers

def cmp(reg1, value2, registers):
    value1 = registers[reg1]

    if value1 < value2:
        registers["111"] = registers["111"][:13] + "1" + registers["111"][14:]

    elif value1 > value2:
        registers["111"] = registers["111"][:14] + "1" + registers["111"][15:]

    elif value1 == value2:
        registers["111"] = registers["111"][:15] + "1"

    return registers

def jmp(label, PC, registers):
    PC = label
    return registers, PC

def jlt(label, PC, registers):
    
    if registers["FLAGS"][13] == 1:
        PC = label

    else:
        PC += 1

    return registers, PC

def jgt(label, PC, registers):
    
    if registers["FLAGS"][14] == 1:
        PC = label

    else:
        PC += 1

    return registers, PC

def je(label, PC, registers):
    
    if registers["FLAGS"][15] == 1:
        PC = label

    else:
        PC += 1

    return registers, PC

def execute(curr_line, PC, registers, halted, memory):
    opcode = curr_line[:5]
    a_opcodes = ["00000", "00001", "00110", "01010", "01011", "01100"]
    b_opcodes = ["00010", "01000", "01001"]
    c_opcodes = ["00011", "00111", "01101", "01110"]
    d_opcodes = ["00100", "00101"]
    e_opcodes = ["01111", "11100", "11101", "11111"]

    if opcode in a_opcodes:
        registers = A(curr_line, registers)
        PC += 1

    elif opcode in b_opcodes:
        registers = B(curr_line, registers)
        PC += 1

    elif opcode in c_opcodes:
        registers = C(curr_line, registers)
        PC += 1

    elif opcode in d_opcodes:
        registers = D(curr_line, registers, memory)
        PC += 1

    elif opcode in e_opcodes:
        registers, PC = E(curr_line, PC, registers)

    else:
        halted = True
        PC += 1

    return PC, halted, registers