#!/usr/bin/env python3

import os

def main():
    with open("input.txt") as f:
        content = f.readlines();
    
    counter = 0    
    
    for line in content :
        digits = line.split('|')[1]
        for mydigit in digits.split() :
            if len(mydigit) in [2,4,3,7] :
                counter += 1
    
    print(counter)


if __name__ == "__main__":
    main()
