#!/usr/bin/env python3

import os

def main():
    with open("input.txt") as f:
            content = f.readline();
    
    strlist = content.split(',')
    fish = [int(i) for i in strlist]

    dayarray = [0,0,0,0,0,0,0,0,0]
    buff = dayarray

    for myday in fish :
        dayarray[myday] += 1
    
    for day in range(256):
        birth = dayarray[0]
        for i in range(8):
            buff[i] = dayarray[i+1]
        buff[6] += birth # parent fish will give birth 6 days later
        buff[8] = birth  # newborn fish will give birth 8 days later
        dayarray = buff

    count = 0
    for myfish in dayarray:
        count += myfish

    print(count)


if __name__ == "__main__":
    main()
