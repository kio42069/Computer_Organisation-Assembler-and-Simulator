import EE

memory = ["0000000000000000" for i in range(128)]
PC = 0
registers = {"000": "0000000000000000", "001": "0000000000000000", "010": "0000000000000000", "011": "0000000000000000",
             "100": "0000000000000000", "101": "0000000000000000", "110": "0000000000000000", "111": "0000000000000000"}

halted = False

with open("test2", 'r') as file:
    lst = file.readlines()

for i in range(len(lst)):
    memory[i] = lst[i][:-1]

while (not halted):
    curr_line = memory[PC].strip()
    PC, halted, registers = EE.execute(curr_line, PC, registers, halted, memory)
    printable_PC = EE.decimal_to_binary(PC)
    num_zeroes = 7 - len(printable_PC)
    for i in range(num_zeroes):
        printable_PC = '0' + printable_PC
    print(printable_PC, end = " ")
    for i in registers.values():
        print(i, end = " ")
    print()

# memory dump
for i in memory:
    # print(i)
    pass
