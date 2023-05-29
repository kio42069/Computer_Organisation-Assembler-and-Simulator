import EE

memory = ["0000000000000000" for i in range(128)]
PC = 0
registers = {"R0": "0000000000000000", "R1": "0000000000000000", "R2": "0000000000000000", "R3": "0000000000000000",
             "R4": "0000000000000000", "R5": "0000000000000000", "R6": "0000000000000000", "FLAGS": "0000000000000000"}

halted = False

with open("test1", 'r') as file:
    lst = file.readlines()

for i in range(len(lst)):
    memory[i] = lst[i]

while (not halted):
    curr_line = memory[PC]
    EE.execute(curr_line, PC, registers)
    # PC.dump(); // Print PC
    # RF.dump(); // Print RF state
    # PC.update(new_PC); // Update PC

# memory dump
for i in memory:
    print(i)
