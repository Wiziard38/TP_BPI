#!/usr/bin/env python3

import sys
from time import time
from random import randint

def tri_insertion(tab):
    for i in range(1, len(tab)):
        for k in range(i,0,-1):
            if tab[k] < tab[k-1]:
                (tab[k], tab[k-1]) = (tab[k-1], tab[k])
            else:
                break

def tri_selection(tab):
    ind = 0
    for i in range(1, len(tab)):
        min = ind
        for k in range(ind + 1, len(tab)):
            if tab[k] < tab[min]:
                min = k
        (tab[ind], tab[k]) = (tab[k], tab[ind])
        ind += 1

def sort(tab):
    tab.sort()

def temps(funct):
    entier = int(sys.argv[1])
    l = [randint(0, entier) for _ in range(entier)]	
    a = time()
    funct(l)
    b = time()
    print(f"le temps de {funct.__name__} est de {b-a}.") 


if __name__ == '__main__':
    temps(tri_insertion)
    temps(tri_selection)
    temps(sort)
