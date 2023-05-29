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

def add(curr_line, PC, registers):

def sub(curr_line, PC, registers):

def mov_i(curr_line, PC, registers):

def mov_r(curr_line, PC, registers):

def ld(curr_line, PC, registers):

def st(curr_line, PC, registers):

def mul(curr_line, PC, registers):

def div(curr_line, PC, registers):

def rs(curr_line, PC, registers):

def ls(curr_line, PC, registers):

def xor(curr_line, PC, registers):

def Or(curr_line, PC, registers):

def And(curr_line, PC, registers):

def Not(curr_line, PC, registers):

def cmp(curr_line, PC, registers):

def jmp(curr_line, PC, registers):

def jlt(curr_line, PC, registers):

def jgt(curr_line, PC, registers):

def je(curr_line, PC, registers):

def hlt(curr_line, PC, registers):

def execute(curr_line, PC, registers):
    match curr_line[:5]:
        case "00000":          
            add(curr_line, PC, registers)

        case "00001":           
            sub(curr_line, PC, registers)

        case "00010":           
            mov_i(curr_line, PC, registers)

        case "00011":          
            mov_r(curr_line, PC, registers)

        case "00100":            
            ld(curr_line, PC, registers)

        case "00101":            
            st(curr_line, PC, registers)

        case "00110":            
            mul(curr_line, PC, registers)

        case "00111":            
            div(curr_line, PC, registers)

        case "01000":            
            rs(curr_line, PC, registers)

        case "01001":            
            ls(curr_line, PC, registers)

        case "01010":            
            xor(curr_line, PC, registers)

        case "01011":            
            Or(curr_line, PC, registers)

        case "01100":            
            And(curr_line, PC, registers)

        case "01101":            
            Not(curr_line, PC, registers)

        case "01110":            
            cmp(curr_line, PC, registers)

        case "01111":            
            jmp(curr_line, PC, registers)

        case "11100":            
            jlt(curr_line, PC, registers)

        case "11101":            
            jgt(curr_line, PC, registers)

        case "11111":            
            je(curr_line, PC, registers)

        case "11010":            
            hlt(curr_line, PC, registers)


