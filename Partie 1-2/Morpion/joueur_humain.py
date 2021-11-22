#!/usr/bin/env python3

import morpion

def joue_coup(cases, symbole):
    """
    Fonction qui va permettre a un joueur humain de jouer son coup au morpion
    """
    # morpion.affiche_plateau(cases)
    while True:
        num_case = input("Dans quelle case voulez vous jouer votre coup (de 1 a 9) ? \n > ")
        if num_case.isnumeric():
            num_case = int(num_case) - 1
            if (-1 < num_case < 9) and cases[num_case] == str(num_case):
                return num_case
        print("Numero invalide, veuillez entrer un numero de case non occupee")
