#!/usr/bin/env python3

import os
import numpy as np

def main():
    with open("input.txt") as f:
           content = f.readlines();

    cave = np.zeros((100,100),dtype=int)

    for row in range(len(content)):
        line = content[row]
        for col in range(len(line) -1):
            digit = int(line[col])
            cave[row,col] = digit
    # print(cave)
    risk = 0
    num_rows, num_cols = cave.shape

    for i in range(num_rows):
        for j in range(num_cols) :
            neighbors = [9,9,9,9] # left, right, top, bottom
            if j > 0 : # left neighbor exists
                neighbors[0] = cave[i,j-1]
            if j < (num_cols -1 ) : # right neighbor exists
                neighbors[1] = cave[i,j+1]
            if i > 0 : # top neighbor exists
                neighbors[2] = cave[i-1,j]
            if i < (num_rows -1) : # bottom neighbor exists
                neighbors[3] = cave[i+1,j]
            #print("coord:",i,j,"value:",cave[i,j], "neighbors:", neighbors)

            if min(neighbors) > cave[i,j] :
                risk += (cave[i,j] + 1)

    print(risk)

if __name__ == "__main__" :
    main()
