#!/usr/bin/env python3

import os

def main():
    with open("input.txt") as f:
            content = f.readline();
    
    strlist = content.split(',')
    fish = [int(i) for i in strlist]

    for day in range(80):
        for fishno in range(len(fish)) :
            newfish = 0
            if fish[fishno] == 0 : # new fish
                newfish += 1
                fish[fishno] = 6
            else :
                fish[fishno] -= 1
            
            for newones in range(newfish) :
                fish.append(8)
        # print(fish)
            
    print(len(fish))


if __name__ == "__main__":
    main()
