#!/usr/bin/env python3

import os

def main():
    with open("input.txt") as f:
            content = f.readlines();

    bitno = (len(content[0]) -1 ) # newline doesn't count!!!
    ones = []
    zeroes = []

    for i in range(0, bitno):
        ones.append(0)
        zeroes.append(0)

    for bitarray in content:
        for bitpos in range(0,bitno) :
            if bitarray[bitpos] == '0' :
                zeroes[bitpos] += 1
            else :
                ones[bitpos] += 1

    print(ones, zeroes)

    gamma = []
    epsilon = []

    for j in range(0,bitno):
        if ones[j] > zeroes[j] :
            gamma.append(1)
            epsilon.append(0)
        else :
            gamma.append(0)
            epsilon.append(1)

    print(gamma, epsilon)
    print(*gamma, sep='')
    print(*epsilon, sep='')


if __name__ == "__main__":
    main()
