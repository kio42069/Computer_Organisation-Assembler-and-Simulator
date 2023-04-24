#Assembler v1

with open("test_case_1.txt", 'r') as f:
    code = f.read()

code_as_lst = code.split('\n')

var_lst = []
output = []

for line in code_as_lst:
    line_lst = line.split()

    line_output = ""

    match line_lst[0]:
        case "var":
            var_lst.append(line_lst[1])

        case "hlt":
            line_output = "1101_0000_0000_0000"

        

        

    output.append(line_output)


to_write = '\n'.join(output)

with open("output_1.txt", 'w') as f:
    f.write(to_write)

print(var_lst)



