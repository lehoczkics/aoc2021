#!/usrbin/env python3

import os

with open("input.txt") as f:
    content = f.readlines()

increased = 0
compares = 0
for i in range(3, len(content)):
    sum1 = (int(content[i-3]) + int(content[i-2]) + int(content[i-1]) )
    sum2 = (int(content[i-2]) + int(content[i-1]) + int(content[i]) )
    print(sum1, sum2)
    if sum2 > sum1 :
        increased += 1
        print("plus1")
    compares += 1

print("increased: ",increased, "compares ", compares)

