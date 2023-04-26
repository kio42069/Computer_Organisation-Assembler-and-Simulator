#Assembler v1

def decimal_to_binary(n):                                    #output is a string
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

def binary_to_decimal(n):                                   #output is an int
    result = 0
    num = str(n)[::-1]

    for i in range(len(num)):
        dig = int(num[i])
        result += dig*(2**i)
    
    return result

def type_A(line_output, line_lst, registers):
    line_output += f"00{registers[line_lst[1]]}{registers[line_lst[2]]}{registers[line_lst[3]]}"
    return line_output

#(e) error handling [ILLEGAL IMMEDIATE VALUES]
def type_B(line_output, line_lst, registers):
    if len(line_lst[-1]) <= 7:
        imm = int(line_lst[2][1:])
        imm = decimal_to_binary(imm)
        line_output += f"0{registers[line_lst[1]]}{imm}"

        return line_output
    else:
        print("Invalid immediate value.")
        return None


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
line_cnt = 0
#(h) error detection [MISSING HLT INSTRUCTION]
if "hlt" not in code_as_lst and "hlt\n" not in code_as_lst:
    print("Missing hlt")

#(i) error detection [HLT NOT LAST INSTRUCTION]
elif "hlt" not in code_as_lst:
    print("hlt not last command")

var_dic = {}
label_dic ={}
output = []

flags_register = "0000_0000_0000_0000"
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}

temp_cnt=0
#(a) error detection done using try except snippets [HANDLE TYPOS]
for line in code_as_lst:
    for_label_lst = line.split()
    match for_label_lst[0][-1]:
        case ":":
            label_dic[for_label_lst[0]] = decimal_to_binary(temp_cnt)     
    temp_cnt+=1       

line_index=0
while line_index<len(code_as_lst):
    flag = True
    line_lst = code_as_lst[line_index].split()
    line_output = ""

    match line_lst[0]:
        case "var":
            print(decimal_to_binary(line_cnt))
            bin_addr = decimal_to_binary(line_cnt)
            var_dic[line_lst[1]] = bin_addr
            line_cnt += 1

        case "hlt":
            line_output = "1101000000000000"

        case "add":                                                                            
            line_output = "00000"
            try:
                line_output = type_A(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "sub":                                                                             
            line_output = "00001"
            try:
                line_output = type_A(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "mov":
            if (line_lst[2][0] == "$"):
                line_output = "00010"
                try:
                    line_output = type_B(line_output, line_lst, registers)
                    if line_output == None:
                        flag = False
                except:
                    print("Typo in instruction. Please check your assembly code again!")


            else:
                line_output = "00011"
                try:
                    line_output = type_C(line_output, line_lst, registers)
                except:
                    print("Typo in instruction. Please check your assembly code again!")


        case "ld":
            line_output = "00100"
            try:
                line_output = type_D(line_output, line_lst, registers)
            except KeyError:
                #(b) error detection [UNDEFINED VARIABLES USED]
                print("Error, use of undeclared variable.")
            except:
                print("Typo in instruction. Please check your assembly code again!")

        case "st":
            line_output = "00101"
            try:
                line_output = type_D(line_output, line_lst, registers)
            except KeyError:
                #(b) error detection [UNDEFINED VARIABLES USED]
                print("Error, use of undeclared variable.")
            except:
                print("Typo in instruction. Please check your assembly code again!")
            
        case "mul":
            line_output = "00110"
            try:
                line_output = type_A(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "div":
            line_output = "00111"
            try:
                line_output = type_C(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "rs":
            line_output = "01000"
            try:
                line_output = type_B(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "ls":
            line_output = "01001"
            try:
                line_output = type_B(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "xor":
            line_output = "01010"
            try:
                line_output = type_A(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "or":
            line_output = "01011"
            line_output = type_A(line_output, line_lst, registers)

        case "and":
            line_output = "01100"
            try:
                line_output = type_A(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "not":
            line_output = "01101"
            try:
                line_output = type_C(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "cmp":
            line_output = "01110"
            try:
                line_output = type_C(line_output, line_lst, registers)
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "jmp":
            line_output = "01111"
            try:
                line_output = type_E(line_output, line_lst)
            except KeyError:
                print("Error, label does not exist.")
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "jlt":
            line_output = "11100"
            try:
                line_output = type_E(line_output, line_lst)
            except KeyError:
                print("Error, label does not exist.")
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "jgt":
            line_output = "11101"
            try:
                line_output = type_E(line_output, line_lst)
            except KeyError:
                print("Error, label does not exist.")
            except:
                print("Typo in instruction. Please check your assembly code again!")


        case "je":
            line_output = "11111"
            try:
                line_output = type_E(line_output, line_lst)
            except KeyError:
                print("Error, label does not exist.")
            except:
                print("Typo in instruction. Please check your assembly code again!")
        #IDK WHAT THIS DOES BUT YEH INF LOOP BANA RAHA AAAAAAAAAA
        case _:
            if line_lst[0][-1] == ":":
                jump_to_addr = binary_to_decimal(label_dic[line_lst[0]])
                # line_index = jump_to_addr-1
            
            else:                 
                print("Error: Operation does not exist")
        

    output.append(line_output) if flag else True
    line_cnt += 1
    line_index += 1

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
print(var_dic)
print(label_dic)

#test commit