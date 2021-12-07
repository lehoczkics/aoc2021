#!/usr/bin/env python3

import os
import numpy as np

def main():
    with open("inputmod.txt") as f:
            content = f.readlines();
    # sea is a 1000 x 1000 matrix of zeroes to store values
    sea = np.zeros((1000,1000), dtype=int)

    # read x1,y1,x2,y2
    for line in content:
        buff = line.split(",")
        x1 = int(buff[0])
        y1 = int(buff[1])
        x2 = int(buff[2])
        y2 = int(buff[3])
    # the logic
        if x1 == x2 :
            if y1 <= y2 :
                for y in range(y1,y2+1):
                    sea[x1,y] += 1
            else :
                for y in range(y2,y1+1):
                    sea[x1,y] += 1
        elif y1 == y2 :
            if x1 <= x2 :
                for x in range(x1,x2+1):
                    sea[x,y1] += 1
            else :
                for x in range(x2,x1+1):
                   sea[x,y1] += 1
        else:
            continue

    print(np.count_nonzero(sea >= 2))

if __name__ == "__main__":
    main()