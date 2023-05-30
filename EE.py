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
    return decimal


def A(curr_line, PC, registers):
    opcode = curr_line[:5]
    reg1 = curr_line[7:10]
    reg2 = curr_line[10:13]
    reg3 = curr_line[13::]
    value2 = binary_to_decimal(str(int(registers[reg2])))
    value3 = binary_to_decimal(str(int(registers[reg3])))
    match opcode:
        case "00000":
            add(value2, value3, reg1, PC, registers)
        
        case "00001":
            sub(value2, value3, reg1, PC, registers)

        case "00110":
            mul(value2, value3, reg1, PC, registers)

        case "01010":
            xor(value2, value3, reg1, PC, registers)
        
        case "01011":
            Or(value2, value3, reg1, PC, registers)

        case "01100":
            And(value2, value3, reg1, PC, registers)

def B(curr_line, PC, registers):
    opcode = curr_line[:5]
    reg = curr_line[6:9]
    imm = curr_line[9::]

    match opcode:
        case "00010":
            mov_i(reg, imm, PC, registers)

        case "01000":
            rs(reg, imm, PC, registers)

        case "01001":
            ls(reg, imm, PC, registers)

def C(curr_line, PC, registers):
    opcode = curr_line[:5]
    reg1 = curr_line[10:13]
    reg2 = curr_line[13::]
    value2 = binary_to_decimal(str(int(registers[reg2])))
    match opcode:
        case "00011":
            mov_r(reg1, value2, PC, registers)

        case "00111":
            div(reg1, value2, PC, registers)

        case "01101":
            Not(reg1, value2, PC, registers)

        case "01110":
            cmp(reg1, value2, PC, registers)

def D(curr_line, PC, registers, memory):
    opcode = curr_line[:5]
    reg = curr_line[6:9]
    var = binary_to_decimal(curr_line[9::])

    match opcode:
        case "00100":
            ld(reg, var, PC, registers, memory)

        case "00101":
            st(reg, var, PC, registers, memory)

def E(curr_line, PC, registers):
    opcode = curr_line[:5]
    label = curr_line[9::]

    match opcode:
        case "01111":
            jmp(label, PC, registers)

        case "11100":
            jlt(label, PC, registers)

        case "11101":
            jgt(label, PC, registers)

        case "11111":
            je(label, PC, registers)

def add(value2, value3, reg1, PC, registers):
    value1 = decimal_to_binary(str(int(value2) + int(value3)))
    if len(value1 > 16):
        registers[reg1] = "0000000000000000"
        registers["FLAGS"] = registers["FLAGS"][:12] + "1" + registers["FLAGS"][13:]
    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1
    PC += 1
    

def sub(value2, value3, reg1, PC, registers):
    value1 = decimal_to_binary(str(int(value2) - int(value3)))
    if len(value1 > 16) or value1 < 0:
        registers[reg1] = "0000000000000000"
        registers["FLAGS"] = registers["FLAGS"][:12] + "1" + registers["FLAGS"][13:]
    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1
    PC += 1
    
def mov_i(reg, imm, PC, registers):
    registers[reg] = imm
    PC += 1

def mov_r(reg1, value2, PC, registers):
    value1 = value2
    registers[reg1] = value1
    PC += 1

def ld(reg, var, PC, registers, memory):
    registers[reg] = memory[int(var)]
    PC += 1

def st(reg, var, PC, registers, memory):
    memory[int(var)] = registers[reg]
    PC += 1

def mul(value2, value3, reg1, PC, registers):
    value1 = decimal_to_binary(str(int(value2) * int(value3)))
    if len(value1 > 16):
        registers[reg1] = "0000000000000000"
        registers["FLAGS"] = registers["FLAGS"][:12] + "1" + registers["FLAGS"][13:]
    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1
    PC += 1

def div(reg1, value2, PC, registers):
    if value2 == 0:
        registers["R0"] = "0000000000000000"
        registers["R1"] = "0000000000000000"
        registers["FLAGS"] = registers["FLAGS"][:12] + "1" + registers["FLAGS"][13:]
    else:
        value1 = registers[reg1]
        quotient = value1 // value2
        remainder = value1 % value2
        registers["R0"] = quotient
        registers["R1"] = remainder
    PC += 1

def rs(reg, imm, PC, registers):
    imm = int(binary_to_decimal(imm))
    value = int(binary_to_decimal(registers[reg]))
    registers[reg] = decimal_to_binary(str(value >> imm))
    PC += 1

def ls(reg, imm, PC, registers):
    imm = int(binary_to_decimal(imm))
    value = int(binary_to_decimal(registers[reg]))
    registers[reg] = decimal_to_binary(str(value << imm))
    PC += 1


def xor(value2, value3, reg1, PC, registers):
    value1 = decimal_to_binary(str(int(value2) ^ int(value3)))
    if len(value1 > 16):
        registers[reg1] = "0000000000000000"
        registers["FLAGS"] = registers["FLAGS"][:12] + "1" + registers["FLAGS"][13:]
    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1
    PC += 1

def Or(value2, value3, reg1, PC, registers):
    value1 = decimal_to_binary(str(int(value2) | int(value3)))
    if len(value1 > 16):
        registers[reg1] = "0000000000000000"
        registers["FLAGS"] = registers["FLAGS"][:12] + "1" + registers["FLAGS"][13:]
    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1
    PC += 1

def And(value2, value3, reg1, PC, registers):
    value1 = decimal_to_binary(str(int(value2) & int(value3)))
    if len(value1 > 16):
        registers[reg1] = "0000000000000000"
        registers["FLAGS"] = registers["FLAGS"][:12] + "1" + registers["FLAGS"][13:]
    else:
        num_zeroes = 16 - len(value1)
        for i in range(num_zeroes):
            value1 = '0' + value1
        registers[reg1] = value1
    PC += 1

def Not(reg1, value2, PC, registers):
    value1 = decimal_to_binary(str(int(~value2)))
    registers[reg1] = value1
    PC += 1

def cmp(reg1, value2, PC, registers):
    value1 = registers[reg1]
    if value1 < value2:
        registers["FLAGS"] = registers["FLAGS"][:13] + "1" + registers["FLAGS"][14:]
    elif value1 > value2:
        registers["FLAGS"] = registers["FLAGS"][:14] + "1" + registers["FLAGS"][15:]
    elif value1 == value2:
        registers["FLAGS"] = registers["FLAGS"][:15] + "1"
    PC += 1
def jmp(label, PC, registers):
    pass

def jlt(label, PC, registers):
    pass

def jgt(label, PC, registers):
    pass

def je(label, PC, registers):
    pass

def hlt(halted):
    halted = True

def execute(curr_line, PC, registers, halted, memory):
    opcode = curr_line[:5]
    a_opcodes = ["00000", "00001", "00110", "01010", "01011", "01100"]
    b_opcodes = ["00010", "01000", "01001"]
    c_opcodes = ["00011", "00111", "01101", "01110"]
    d_opcodes = ["00100", "00101"]
    e_opcodes = ["01111", "11100", "11101", "11111"]
    

    if opcode in a_opcodes:
        A(curr_line, PC, registers)

    elif opcode in b_opcodes:
        B(curr_line, PC, registers)

    elif opcode in c_opcodes:
        C(curr_line, PC, registers)

    elif opcode in d_opcodes:
        D(curr_line, PC, registers, memory)

    elif opcode in e_opcodes:
        E(curr_line, PC, registers)

    else:
        hlt(halted)