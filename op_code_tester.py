lst = ["00000", "00001", "00110", "01010", "01011", "01100", "00010",
       "01000", "01001", "00011", "00111", "01101", "01110", "00100", "00101",
       "01111", "11100", "11101", "11111"]

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    opcode = str(i)+str(j)+str(k)+str(l)+str(m)
                    if (opcode not in lst):
                        print(opcode)
