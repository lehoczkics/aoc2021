#!/usr/bin/env python3

import os

def counter(arr, bitpos) :
    zeroes = 0
    ones = 0
    
    for myline in arr:
        if myline[bitpos] == '0' :
            zeroes += 1
        else :
            ones += 1
    return zeroes, ones;

def main():
    with open("input.txt") as f:
            content = f.readlines();

    oxigen = content.copy()
    co2 = content.copy()
    oxigenvalue = '' # it is a string haha
    co2value = ''

    i = 0
    while len(oxigen) > 1 :
        zeroes,ones = counter(oxigen,i)
        print(zeroes, ones)

        if ones > zeroes :
            oxigenvalue = oxigenvalue + '1'
        elif ones == zeroes :
            oxigenvalue = oxigenvalue + '1'
        else :
            oxigenvalue = oxigenvalue + '0'
        
        print("Oxigenvalue:", oxigenvalue)
        oxigen[:] = [s for s in oxigen if s.startswith(oxigenvalue)]
        i += 1
    print(oxigen)
        
    j = 0
    while len(co2) > 1 :
        zeroes,ones = counter(co2,j)
        print(zeroes, ones)

        if ones < zeroes :
            co2value = co2value + '1'
        elif ones == zeroes :
            co2value = co2value + '0'
        else :
            co2value = co2value + '0'
        
        print("CO2value:", co2value)
        co2[:] = [s for s in co2 if s.startswith(co2value)]
        j += 1
    print(co2)

if __name__ == "__main__":
    main()