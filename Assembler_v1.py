#Assembler v1

# def type_A():


# def type_B():


# def type_C():


# def type_D():


def type_E(line_output, line_lst):
    line_output += "0000"
    line_output += line_lst[1]

    return line_output


with open("test_case_1.txt", 'r') as f:
    code = f.read()

code_as_lst = code.split('\n')

#to remove all empty lines
for i in range(0, len(code_as_lst) - 1):
    if (code_as_lst[i] == ""):
        code_as_lst.pop(i)

var_lst = []
output = []

for line in code_as_lst:
    line_lst = line.split()

    line_output = ""

    match line_lst[0]:
        case "var":
            var_lst.append(line_lst[1])

        case "hlt":
            line_output = "1101000000000000"

        # case "add":

        # case "sub":

        # case "mov":

        # case "ld":

        # case "st":

        # case "mul":

        # case "div":

        # case "rs":

        # case "ls":

        # case "xor":

        # case "or":

        # case "and":

        # case "not":

        # case "cmp":

        case "jmp":
            line_output = "01111"
            line_output = type_E(line_output, line_lst)


        case "jlt":
            line_output = "11100"
            line_output = type_E(line_output, line_lst)


        case "jgt":
            line_output = "11101"
            line_output = type_E(line_output, line_lst)


        case "je":
            line_output = "11111"
            line_output = type_E(line_output, line_lst)

        case _:
            print("Error: Operation does not exist")

    output.append(line_output)


#to delete empty lines from output
for i in range(0, len(output) - 1):
    if (output[i] == ""):
        output.pop(i)

to_write = '\n'.join(output)

with open("output_1.txt", 'w') as f:
    f.write(to_write)

print(var_lst)



