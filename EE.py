#decimal to binary
def decimal_to_binary(number):
    return bin(int(number))[2:]

#binary to decimal
def binary_to_binary(number):
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
    match opcode:
        case "00000":
            add(reg1, reg2, reg3, PC, registers)
        
        case "00001":
            sub(reg1, reg2, reg3, PC, registers)

        case "00110":
            mul(reg1, reg2, reg3, PC, registers)

        case "01010":
            xor(reg1, reg2, reg3, PC, registers)
        
        case "01011":
            Or(reg1, reg2, reg3, PC, registers)

        case "01100":
            And(reg1, reg2, reg3, PC, registers)

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

    match opcode:
        case "00011":
            mov_r(reg1, reg2, PC, registers)

        case "00111":
            div(reg1, reg2, PC, registers)

        case "01101":
            Not(reg1, reg2, PC, registers)

        case "01110":
            cmp(reg1, reg2, PC, registers)

def D(curr_line, PC, registers):
    opcode = curr_line[:5]
    reg = curr_line[6:9]
    var = curr_line[9::]

    match opcode:
        case "00100":
            ld(reg, var, PC, registers)

        case "00101":
            st(reg, var, PC, registers)

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

def add(reg1, reg2, reg3, PC, registers):

def sub(reg1, reg2, reg3, PC, registers):

def mov_i(reg, imm, PC, registers):

def mov_r(reg1, reg2, PC, registers):

def ld(reg, var, PC, registers):

def st(reg, var, PC, registers):

def mul(reg1, reg2, reg3, PC, registers):

def div(reg1, reg2, PC, registers):

def rs(reg, imm, PC, registers):

def ls(reg, imm, PC, registers):

def xor(reg1, reg2, reg3, PC, registers):

def Or(reg1, reg2, reg3, PC, registers):

def And(reg1, reg2, reg3, PC, registers):

def Not(reg1, reg2, PC, registers):

def cmp(reg1, reg2, PC, registers):

def jmp(label, PC, registers):

def jlt(label, PC, registers):

def jgt(label, PC, registers):

def je(label, PC, registers):

def hlt(halted):

def execute(curr_line, PC, registers, halted):
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
        D(curr_line, PC, registers)
    elif opcode in e_opcodes:
        E(curr_line, PC, registers)
    else:
        hlt(halted)