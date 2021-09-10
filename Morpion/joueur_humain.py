#!/usr/bin/env python3

import morpion

def joue_coup(cases, symbole):
    """
    Fonction qui va permettre a un joueur humain de jouer son coup au morpion
    """
    morpion.affiche_plateau(cases)
    while True:
        num_case = int(input("Dans quelle case voulez vous jouer votre coup ? \n > "))
        if cases[num_case] == num_case:
            return num_case
        else:
            print("Numero invalide, veuillez entrer un numero de case non occupee")
