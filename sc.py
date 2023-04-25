#Assembler v1

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
    line_output += f"0{registers[line_lst[1]]}{var_dic[line_lst[2]]}"
    return line_output


def type_E(line_output, line_lst):
    line_output += "0000"
    line_output += line_lst[1]

    return line_output


with open("test_case_1.txt", 'r') as f:
    code_as_lst = f.readlines()

line_cnt=0
#to remove all empty lines
if (code_as_lst):
    for i in range(0, len(code_as_lst) - 1):
        if (code_as_lst[i] == ""):
            code_as_lst.pop(i)
        elif (code_as_lst[0:3] != "var"):
            line_cnt+=1

var_dic = {}
label_dic ={}
output = []

flags_register = "0000_0000_0000_0000"
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}

for line in code_as_lst:
    for_label_lst = line.split()
    match for_label_lst[0][-1]:
        case _:
            

temp_cnt = 0
for line in code_as_lst:
    line_lst = line.split()
    line_output = ""


    match line_lst[0]:
        case "var":
            bin_addr = decimal_to_binary(line_cnt)
            var_dic[line_lst[1]] = bin_addr
            line_cnt += 1

        case "hlt":
            line_output = "1101000000000000"

        case "add":                                                                            
            line_output = "00000"
            line_output = type_A(line_output, line_lst, registers)

        case "sub":                                                                             
            line_output = "00001"
            line_output = type_A(line_output, line_lst, registers)

        case "mov":
            if (line_lst[2][0] == "$"):
                line_output = "00010"
                line_output = type_B(line_output, line_lst, registers)

            else:
                line_output = "00011"
                line_output = type_C(line_output, line_lst, registers)

        case "ld":
            line_output = "00100"
            line_output = type_D(line_output, line_lst, registers)

        case "st":
            line_output = "00101"
            try:
                line_output = type_D(line_output, line_lst, registers)
            except KeyError:
                print("Error, use of undeclared variable.")
        case "mul":
            line_output = "00110"
            line_output = type_A(line_output, line_lst, registers)

        case "div":
            line_output = "00111"
            line_output = type_C(line_output, line_lst, registers)

        case "rs":
            line_output = "01000"
            line_output = type_B(line_output, line_lst, registers)

        case "ls":
            line_output = "01001"
            line_output = type_B(line_output, line_lst, registers)

        case "xor":
            line_output = "01010"
            line_output = type_A(line_output, line_lst, registers)

        case "or":
            line_output = "01011"
            line_output = type_A(line_output, line_lst, registers)

        case "and":
            line_output = "01100"
            line_output = type_A(line_output, line_lst, registers)

        case "not":
            line_output = "01101"
            line_output = type_C(line_output, line_lst, registers)

        case "cmp":
            line_output = "01110"
            line_output = type_C(line_output, line_lst, registers)

        case "jmp":
            line_output = "01111"
            try:
                line_output = type_E(line_output, line_lst)
            except:
                print("Error, label does not exist")


        case "jlt":
            line_output = "11100"
            try:
                line_output = type_E(line_output, line_lst)


        case "jgt":
            line_output = "11101"
            line_output = type_E(line_output, line_lst)


        case "je":
            line_output = "11111"
            line_output = type_E(line_output, line_lst)

        case _:
            if line_lst[0][-1] == ":":
                label_dic[line_lst[0]] = decimal_to_binary(temp_cnt)
            
            else:                 
                print("Error: Operation does not exist")
        

    output.append(line_output)
    temp_cnt+=1

#to delete empty lines from output
if (output):
    del_counter=0
    while len(output)>del_counter:
        if (output[del_counter] == ""):
            output.pop(del_counter)
        else:
            del_counter+=1

to_write = '\n'.join(output)

with open("output_1.txt", 'w') as f:
    f.write(to_write)

print(label_dic)
