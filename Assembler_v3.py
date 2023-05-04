#Assembler v3

# ld and st (type D) use variables
# jump instructions (type E) use labels
# all instructions using mem_addr use labels/vars


#global errors list
errors = []

#global dicts
variables = {}          #"var_name":"var_address"
labels = {}             #"label_name":"label_address"
output = {}             #"line_number":"binary_code"

flags_register = "0000_0000_0000_0000"
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}

def decimal_to_binary(n):
    output_binary_code = bin(n)[2:]
    return output_binary_code


#3 register type
def type_A(line_output, line_lst, registers):
    register1 = line_lst[1]
    register2 = line_lst[2]
    register3 = line_lst[3]

    if (register1 not in registers) or (register2 not in registers) or (register3 not in registers):
        errors.append("ERROR : Invalid Register")
        return "ERROR"

    line_output += f"00{registers[register1]}{registers[register2]}{registers[register3]}"
    return line_output


#register and immediate type
def type_B(line_output, line_lst, registers):

    register = line_lst[1]

    if register not in registers:
        errors.append("ERROR : Invalid Register")
        return "ERROR"

    imm = int(line_lst[2][1:])

    if (imm < 0) or (imm > 127):
        errors.append("ERROR : Illegal Immediate Value")
        return "ERROR"

    imm = decimal_to_binary(imm)

    length_of_imm_to_be_added = 7 - len(imm)       # handle overflow of 7 bits just before here pls
    for i in range(length_of_imm_to_be_added):
        imm = '0' + imm

    line_output += f"0{registers[register]}{imm}"

    return line_output


#2 register type
def type_C(line_output, line_lst, registers):
    register1 = line_lst[1]
    register2 = line_lst[2]

    if (register1 not in registers) or (register2 not in registers):
        errors.append("ERROR : Invalid Register")
        return "ERROR"
    
    line_output += f"00000{registers[register1]}{registers[register2]}"
    return line_output


#register and memory address type (variable)
def type_D(line_output, line_lst):
    register = line_lst[1]

    if register not in registers:
        errors.append("ERROR : Invalid Register")
        return "ERROR"
        
    variable = line_lst[2]

    if variable not in variables:
        if variable not in labels:
            errors.append("ERROR : Undefined Variable")
            return "ERROR"
        
        else:
            errors.append("ERROR : Misuse of label as variable")
            return "ERROR"
        
    line_output += f"0{registers[register]}{variables[variable]}"
    return line_output


#memory address type (jump to a label)
def type_E(line_output, line_lst):
    line_output += "0000"

    label = line_lst[1]
    if label not in labels:
        if label not in variables:
            errors.append("ERROR : Undefined Label")
            return "ERROR"
        
        else:
            errors.append("ERROR : Misuse of variable as label")
            return "ERROR"
        
    line_output += labels[line_lst[1]]
    return line_output


with open("test_case_1.txt", 'r') as f:
    code_as_lst = f.readlines()

#removing empty lines from code_as_lst
if (code_as_lst):
    i = 0
    while(i < len(code_as_lst)):
        if (code_as_lst[i] == "" or code_as_lst[i] == "\n"):
            code_as_lst.pop(i)
        else:
            i += 1

#checking all variable declarations are at beginning of program
index = 0

while(code_as_lst[index][:3] == 'var'):
    index += 1

while(index < len(code_as_lst)):
    if code_as_lst[index][:3] == 'var':
        errors.append("ERROR : Variable Declaration must be at the beginning")
        break
    index += 1

# pass 1
"""
- count lines in the code
- detect labels and vars
- build dicts variables and labels
- check for errors
- initialise entries of output dictionary
"""

line_counter = 0

for line in code_as_lst:
    line_lst = line.split()

    line_output = ""

    match line_lst[0]:
        case "var":
            variables[line_lst[1]] = "Initialised"        #initialising variable when detected

        case "hlt":
            line_output = "1101000000000000"
            line_counter += 1

        #type A instructions
        case "add":                                                                            
            line_output = "00000"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "sub":                                                                             
            line_output = "00001"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "mul":
            line_output = "00110"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "xor":
            line_output = "01010"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "or":
            line_output = "01011"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "and":
            line_output = "01100"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        #type B instructions
        case "mov":
            if (line_lst[2][0] == "$"):
                line_output = "00010"
                line_output = type_B(line_output, line_lst, registers)
                line_counter += 1

            else:       #type C (there are two mov instructions)                                                  
                line_output = "00011"
                line_output = type_C(line_output, line_lst, registers)
                line_counter += 1

        case "rs":
            line_output = "01000"
            line_output = type_B(line_output, line_lst, registers)
            line_counter += 1

        case "ls":
            line_output = "01001"
            line_output = type_B(line_output, line_lst, registers)
            line_counter += 1

        #type C instructions
        case "div":
            line_output = "00111"
            line_output = type_C(line_output, line_lst, registers)
            line_counter += 1

        case "not":
            line_output = "01101"
            line_output = type_C(line_output, line_lst, registers)
            line_counter += 1

        case "cmp":
            line_output = "01110"
            line_output = type_C(line_output, line_lst, registers)
            line_counter += 1

        #type D instructions
        case "ld":
            line_output = "00100"
            line_output = type_D(line_output, line_lst)
            line_counter += 1

        case "st":
            line_output = "00101"
            line_output = type_D(line_output, line_lst)
            line_counter += 1

        #type E instructions
        case "jmp":
            line_output = "01111"
            line_output = type_E(line_output, line_lst)
            line_counter += 1

        case "jlt":
            line_output = "11100"
            line_output = type_E(line_output, line_lst)
            line_counter += 1

        case "jgt":
            line_output = "11101"
            line_output = type_E(line_output, line_lst)
            line_counter += 1

        case "je":
            line_output = "11111"
            line_output = type_E(line_output, line_lst)
            line_counter += 1

        #default case and label check
        case _:
            if (line_lst[0][-1] == ':'):                                #key-value pair is label-address in 7-bit binary
                temp_addr = decimal_to_binary(line_counter)
                temp_addr = "0"*(7 - len(temp_addr)) + temp_addr
                labels[line_lst[0][:-1]] = temp_addr
                line_counter += 1

            else:
                print(line_lst)
                errors.append("Error: Illegal Operation")

# pass 2
"""
- replace labels and vars with their addresses
- update entries of output dictionary
"""



print(errors)
print(variables)
print(labels)