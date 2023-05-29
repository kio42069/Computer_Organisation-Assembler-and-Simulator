import EE

memory = ["0000000000000000" for i in range(128)]
PC = 0
registers = {"R0": 0, "R1": 0, "R2": 0, "R3": 0,
             "R4": 0, "R5": 0, "R6": 0, "FLAGS": 0}

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
