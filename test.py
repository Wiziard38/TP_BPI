#!/usr/bin/env python3

def get_bits(entier):
    list_bin = []
    while entier:
        if entier & 1 == 0:
            list_bin.insert(0, 0)
        else:
            list_bin.insert(0, 1)
        entier = entier >> 1
    return list_bin

def mult_bin(entier1, entier2):
    l1 = get_bits(entier1)
    l2 = get_bits(entier2)

    if len(l1) > len(l2):
        (l1, l2) = (l2, l1)
    
    for k in range(len(l2), 0, -1):
        ...

import sys
print(get_bits(int(sys.argv[1])))