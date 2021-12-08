#!/usr/bin/env python3

import os

def main():
    with open("input.txt") as f:
            content = f.readline();
    
    strlist = content.split(',')
    crabs = [int(i) for i in strlist]

    farest = max(crabs)
    fuels = []

    for i in range(farest):
        fuel = 0
        for mycrab in crabs :
            dist = abs(i - mycrab)
            myfuel = dist * (dist +1) /2
            fuel += myfuel
        
        fuels.append(fuel)
    
    print(min(fuels))


if __name__ == "__main__":
    main()