#Assembler v1

# ld and st (type D) use variables
# jump instructions (type E) use labels


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


def type_A(line_output, line_lst, registers):
    line_output += f"00{registers[line_lst[1]]}{registers[line_lst[2]]}{registers[line_lst[3]]}"
    return line_output


def type_B(line_output, line_lst, registers):
    imm = int(line_lst[2][1:])
    imm = decimal_to_binary(imm)
    line_output += f"0{registers[line_lst[1]]}{imm}"

    return line_output


def type_C(line_output, line_lst, registers):
    line_output += f"00000{registers[line_lst[1]]}{registers[line_lst[2]]}"
    return line_output


def type_D(line_output, line_lst, registers):
    line_output += f"0{registers[line_lst[1]]}{line_lst[2]}"
    return line_output


def type_E(line_output, line_lst):
    line_output += "0000"
    line_output += line_lst[1]

    return line_output


with open("test_case_1.txt", 'r') as f:
    code_as_lst = f.readlines()

#to remove all empty lines - WRONG CODE; NEEDS CORRECTION
if (code_as_lst):
    for i in range(0, len(code_as_lst) - 1):
        if (code_as_lst[i] == ""):
            code_as_lst.pop(i)

variables = {}
labels = {}
output = []
line_counter = 0

flags_register = "0000_0000_0000_0000"
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}

for line in code_as_lst:
    line_lst = line.split()

    line_output = ""

    match line_lst[0]:
        case "var":
            variables[line_lst[1]].append("0")

        case "hlt":
            line_output = "1101000000000000"
            line_counter += 1

        case "add":                                                                            
            line_output = "00000"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "sub":                                                                             
            line_output = "00001"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "mov":
            if (line_lst[2][0] == "$"):
                line_output = "00010"
                line_output = type_B(line_output, line_lst, registers)
                line_counter += 1

            else:
                line_output = "00011"
                line_output = type_C(line_output, line_lst, registers)
                line_counter += 1

        case "ld":
            line_output = "00100"
            line_output = type_D(line_output, line_lst, registers)
            line_counter += 1

        case "st":
            line_output = "00101"
            line_output = type_D(line_output, line_lst, registers)
            line_counter += 1

        case "mul":
            line_output = "00110"
            line_output = type_A(line_output, line_lst, registers)
            line_counter += 1

        case "div":
            line_output = "00111"
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

        case "not":
            line_output = "01101"
            line_output = type_C(line_output, line_lst, registers)
            line_counter += 1

        case "cmp":
            line_output = "01110"
            line_output = type_C(line_output, line_lst, registers)
            line_counter += 1

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

        case _:
            if (line_lst[0][-1] == ':'):
                labels[line_lst[0]].append("0")

            else:
                print("Error: Operation does not exist")

    output.append(line_output)


#to delete empty lines from output - WRONG CODE; NEEDS CORRECTION
if (output):
    for i in range(0, len(output) - 1):
        if (output[i] == ""):
            output.pop(i)

to_write = '\n'.join(output)

with open("output_1.txt", 'w') as f:
    f.write(to_write)

print(variables)