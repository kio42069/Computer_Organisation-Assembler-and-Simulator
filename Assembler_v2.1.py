#Assembler v2

# ld and st (type D) use variables
# jump instructions (type E) use labels
# all instructions using mem_addr use labels/vars


#global errors list
errors = []

def decimal_to_binary(n):
    output_binary_code = bin(n)[2:]
    return output_binary_code

#3 register type
def type_A(line_output, line_lst, registers):
    register1 = line_lst[1]
    register2 = line_lst[2]
    register3 = line_lst[3]
    if register1 not in registers or register2 not in registers or register3 not in registers:
        errors.append("ERROR : Incorrect register name")
    line_output += f"00{registers[line_lst[1]]}{registers[line_lst[2]]}{registers[line_lst[3]]}"
    return line_output


#register and immediate type
def type_B(line_output, line_lst, registers):
    register = line_lst[1]
    if register not in registers:
        errors.append("ERROR : Incorrect register name")
    imm = int(line_lst[2][1:])
    imm = decimal_to_binary(imm)
    if len(imm) > 7:
        errors.append("Illegal Immdiate value")
    length_of_imm_to_be_added = 7 - len(imm)       # handle overflow of 7 bits just before here pls
    for i in range(length_of_imm_to_be_added):
        imm = '0' + imm
    line_output += f"0{registers[line_lst[1]]}{imm}"  

    return line_output


#2 register type
def type_C(line_output, line_lst, registers):
    register1 = line_lst[1]
    register2 = line_lst[2]
    if register1 not in registers or register2 not in registers:
        errors.append("ERROR : Incorrect register name")
    line_output += f"00000{registers[line_lst[1]]}{registers[line_lst[2]]}"
    return line_output


#register and memory address type (variable)
def type_D(line_output, line_lst):
    register = line_lst[1]
    if register not in registers:
        errors.append("ERROR : Incorrect register name")
    variable = line_lst[2]
    if variable not in variables:
        if variable not in labels and variable + ":" not in labels:
            errors.append("ERROR : Using undefined variable")
        else:
            errors.append("ERROR : Misuse of label as variable")
    line_output += f"0{registers[line_lst[1]]}{variables[line_lst[2]]}"
    return line_output


#memory address type (jump to a label)
def type_E(line_output, line_lst):
    line_output += "0000"
    label = line_lst[1]
    if label not in labels:
        if label not in variables and label[:len(label)-1] not in variables:
            errors.append("ERROR : Using undefined label")
        else:
            errors.append("ERROR : Misuse of variable as label")
    line_output += labels[line_lst[1]]
    return line_output


with open("test_case_1.txt", 'r') as f:
    code_as_lst = f.readlines()



variables = {}          #"var_name":"var_address"
labels = {}             #"label_name":"label_address"
output = {}             #"line_number":"binary_code"
line_counter = 0

flags_register = "0000_0000_0000_0000"
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}

#removing empty lines from code_as_lst
if (code_as_lst):
    i = 0
    while(i < len(code_as_lst)):
        if (code_as_lst[i] == "" or code_as_lst[i] == "\n"):
            code_as_lst.pop(i)
        else:
            i += 1

index = 0
while(code_as_lst[index][:3] == 'var'):
    index += 1
while(index < len(code_as_lst)):
    if code_as_lst[index][:3] == 'var':
        errors.append("ERROR : All variables not declared at the beginning")
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

for line in code_as_lst:
    line_lst = line.split()

    match line_lst[0]:
        case "var":
            variables[line_lst[1]] = "0"

        case "hlt":
            line_counter += 1

        #type A instructions
        case "add":                                                                            
            line_counter += 1

        case "sub":                                                                             
            line_counter += 1

        case "mul":
            line_counter += 1

        case "xor":
            line_counter += 1

        case "or":
            line_counter += 1

        case "and":
            line_counter += 1


        #type B instructions
        case "mov":
            line_counter += 1

        case "rs":
            line_counter += 1

        case "ls":
            line_counter += 1


        #type C instructions
        case "div":
            line_counter += 1

        case "not":
            line_counter += 1

        case "cmp":
            line_counter += 1


        #type D instructions
        case "ld":
            line_counter += 1

        case "st":
            line_counter += 1


        #type E instructions
        case "jmp":
            line_counter += 1

        case "jlt":
            line_counter += 1

        case "jgt":
            line_counter += 1

        case "je":
            line_counter += 1


        #default case and label check
        case _:
            if (line_lst[0][-1] == ':'):                                #key-value pair is label-address in 7-bit binary
                temp_addr = decimal_to_binary(line_counter)
                temp_addr = "0"*(7 - len(temp_addr)) + temp_addr
                labels[line_lst[0]] = temp_addr
                line_counter += 1

            else:
                print(line_lst)
                errors.append("Error: Operation does not exist")

print(variables)
print(labels)

# pass 2
"""
- replace labels and vars with their addresses
- update entries of output dictionary
"""
temp_cnt = 0

for line in code_as_lst:
    line_lst = line.split()

    temp_lst = line_lst

    line_output = ""

    #replacing variables with their 7-bit addresses (zero based indexing), as they are encountered
    if (line_lst[0] == "var") and (line_lst[1] in variables.keys()):
        address = decimal_to_binary(line_counter)
        address = "0"*(7 - len(address)) + address
        variables[line_lst[1]] = address
        line_counter += 1

    elif (line_lst[0][-1] == ":"):
        dec_addr = labels[line_lst[0]]
        temp_cnt = int(dec_addr,2) + 1
        temp_lst = line_lst[1:]
    
    #match case to manipulate changes in labels and variables, removed counter as temp counter would be sufficient
    match temp_lst[0]:

        case "hlt":
            line_output = "1101000000000000"

        #type A instructions
        case "add":
            line_output = "00000"
            line_output = type_A(line_output, temp_lst, registers)

        case "sub":                                                                             
            line_output = "00001"
            line_output = type_A(line_output, temp_lst, registers)

        case "mul":
            line_output = "00110"
            line_output = type_A(line_output, temp_lst, registers)

        case "xor":
            line_output = "01010"
            line_output = type_A(line_output, temp_lst, registers)

        case "or":
            line_output = "01011"
            line_output = type_A(line_output, temp_lst, registers)

        case "and":
            line_output = "01100"
            line_output = type_A(line_output, temp_lst, registers)

        #type B instructions
        case "mov":
            if (temp_lst[2][0] == "$"):
                line_output = "00010"
                line_output = type_B(line_output, temp_lst, registers)

            else:       #type C (there are two mov instructions)                                                  
                line_output = "00011"
                line_output = type_C(line_output, temp_lst, registers)

        case "rs":
            line_output = "01000"
            line_output = type_B(line_output, temp_lst, registers)

        case "ls":
            line_output = "01001"
            line_output = type_B(line_output, temp_lst, registers)


        #type C instructions
        case "div":
            line_output = "00111"
            line_output = type_C(line_output, temp_lst, registers)

        case "not":
            line_output = "01101"
            line_output = type_C(line_output, temp_lst, registers)

        case "cmp":
            line_output = "01110"
            line_output = type_C(line_output, temp_lst, registers)

        #type D instructions
        case "ld":
            line_output = "00100"
            line_output = type_D(line_output, temp_lst)

        case "st":
            line_output = "00101"
            line_output = type_D(line_output, temp_lst)

        #type E instructions
        case "jmp":
            line_output = "01111"
            line_output = type_E(line_output, temp_lst)

        case "jlt":
            line_output = "11100"
            line_output = type_E(line_output, temp_lst)

        case "jgt":
            line_output = "11101"
            line_output = type_E(line_output, temp_lst)

        case "je":
            line_output = "11111"
            line_output = type_E(line_output, temp_lst)


        #default case
        case _:
            errors.append("Error: Operation does not exist")

    output[temp_cnt] = line_output
    #creating a temp counter (doesn't follow zero based indexing)
    if (line_lst[0] != "var"):    
        temp_cnt += 1


# Missing HLT instruction
binary_instruction_values = output.values()
if "1101000000000000" not in binary_instruction_values:
    errors.append("ERROR : Missing hlt instruction")
elif list(binary_instruction_values).index("1101000000000000") != len(binary_instruction_values)-1:
    errors.append("ERROR : hlt not last instruction")


#code to merge the binary code, ie. values of output dictionary
to_write = ""
for i in output:
    to_write += str(i) + " : " + str(output[i]) + "\n"

with open("output_1.txt", 'w') as f:
    f.write(to_write)

print(errors)
print(variables)
print(labels)