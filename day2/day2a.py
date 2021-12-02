#!/usr/bin/env python3

import os

def main():
    with open("input.txt") as f:
            content = f.readlines();

    depth=0
    forw=0

    for i in range(0,len(content)):
        where = content[i].split()
        if where[0] == 'forward':
            forw += int(where[1])
        elif where[0] == 'down' :
            depth += int(where[1])
        elif where[0] == 'up':
            depth -= int(where[1])

    print("depth: ",depth,"forward: ",forw,"multiplied: ",forw*depth)

if __name__ == "__main__":
    main()
