#!/usrbin/env python3

import os

with open("input.txt") as f:
    content = f.readlines()

increased = 0
compares = 0
for i in range(1, len(content)):
    compares += 1
    #print("prev ", content[i-1], "actual ", content[i])
    if int(content[i-1]) < int(content[i]) :
        increased += 1
        #print("increased: ", increased)

print("increased: ",increased, "compares ", compares)

