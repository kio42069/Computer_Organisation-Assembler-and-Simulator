#Assembler v1

# ld and st (type D) use variables
# jump instructions (type E) use labels
# all instructions using mem_addr use labels/vars

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


#3 register type
def type_A(line_output, line_lst, registers):
    line_output += f"00{registers[line_lst[1]]}{registers[line_lst[2]]}{registers[line_lst[3]]}"
    return line_output


#register and immediate type
def type_B(line_output, line_lst, registers):
    imm = int(line_lst[2][1:])
    imm = decimal_to_binary(imm)
    line_output += f"0{registers[line_lst[1]]}{imm}"

    return line_output


#2 register type
def type_C(line_output, line_lst, registers):
    line_output += f"00000{registers[line_lst[1]]}{registers[line_lst[2]]}"
    return line_output


#register and memory address type (variable)
def type_D(line_output, line_lst):
    line_output += f"0{registers[line_lst[1]]}{variables[line_lst[2]]}"
    return line_output


#memory address type (jump to a label)
def type_E(line_output, line_lst):
    line_output += "0000"
    line_output += labels[line_lst[1]]

    return line_output


with open("test_case_1.txt", 'r') as f:
    code_as_lst = f.readlines()

# code to remove empty lines from input

variables = {}          #"var_name":"var_address"
labels = {}             #"label_name":"label_address"
output = {}             #"line_number":"binary_code"
line_counter = 0

flags_register = "0000_0000_0000_0000"
registers = {"R0": "000", "R1": "001", "R2": "010", "R3": "011", "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}

# pass 1
"""
- count lines in the code
- detect labels and vars
- build dicts variables and labels
- check for errors
- initialise entries of output dictionary
"""

# pass 2
"""
- replace labels and vars with their addresses
- update entries of output dictionary
"""

#code to merge the binary code, ie. values of output dictionary
to_write = ""

with open("output_1.txt", 'w') as f:
    f.write(to_write)


# for testing pr
print(variables)
print("\n")
print(labels)
print("\n")
print(output)