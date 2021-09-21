#!/usr/bin/env python3

def get_bits(entier):
    """
    Renvoie une liste de la representation de l'entier donne en binaire.
    """
    list_bin = []
    while entier:
        if entier & 1 == 0:
            list_bin.insert(0, 0)
        else:
            list_bin.insert(0, 1)
        entier = entier >> 1
    return list_bin


def mult_bin(entier1, entier2):
    """
    Multiplie deux entiers entre eux, representes de maniere binaire, selon a methode vue en primaire.
    """
    l1 = get_bits(entier1)
    l2 = get_bits(entier2)
    res = []

    for i in range(len(l1)-1 , -1, -1): # Parcours en sens inverse
        if l1[i] == 1:
            list_tmp = l2.copy()
            for k in range(len(l1)-i-1):
                list_tmp.append(0)
            res = add_bin(res, list_tmp)

    return res        



def add_bin(list1, list2):
    """
    Fonction qui realise l'addition binaire de deux entiers representes sous forme de listes.
    """    
    list_res = []
    retenue = 0
    
    # On met sur la meme longueur
    if len(list2) != len(list1):
        if len(list2) > len(list1):
            for k in range(len(list2)-len(list1)):
                list1.insert(0,0)
        else:
            for k in range(len(list1)-len(list2)):
                list1.insert(0,0)
    
    for i in range(len(list2)-1,-1,-1):
        somme = list1[i] + list2[i]
        if somme == 0:
            if retenue == 1:
                list_res.insert(0, 1)
                retenue = 0
            else:
                list_res.insert(0, 0)
        elif somme == 1:
            if retenue == 1:
                list_res.insert(0, 0)
                retenue = 1
            else:
                list_res.insert(0, 1)
        else:
            if retenue == 1:
                list_res.insert(0, 1)
            else:
                list_res.insert(0, 0)
                retenue = 1

    # Ce qui reste dans l'entier 1
    for k in range(len(list1)-len(list2)-1, -1, -1):
        if retenue == 0:
            list_res.insert(0, list1[k])
        else:
            if list1[k] == 1:
                list_res.insert(0, 0)
            else:
                list_res.insert(0, 1)
                retenue = 0

    if retenue == 1:
        list_res.insert(0, 1)

    return list_res

import sys
print( mult_bin(int(sys.argv[1]), int(sys.argv[2]) ) )