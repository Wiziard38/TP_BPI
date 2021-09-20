def int_to_bin(entier):
    list_bin = []
    while entier:
        if entier & 1 == 0:
            list_bin.insert(0, 0)
        else:
            list_bin.insert(0, 1)
        entier >> 1
    return list_bin

import sys


print(int_to_bin(sys.argv[2]))