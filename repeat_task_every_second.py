# import os, time
# while 1:
#     os.system("py Assembler_v4.py")
#     time.sleep(0.1)

import os
for i in range(1,31):
    src = "hardBinTests\\"+str(i)+".txt"
    dst = "hardBinTests\\test"+str(i)+".txt"
    os.rename(src, dst)