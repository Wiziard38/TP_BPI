#!/usr/bin/env python3

import sys
import os
os.chdir("/Users/mathis/Desktop/TP_BPI/lights_out/")

def jeu(niveau):
    """
    Fonction qui va faire jouer l'utilisateur. 
    """

    # Initialisation du plateau
    plateau = []
    fichier = open(niveau, 'r')
    for ligne in fichier:
        plateau.append(list(ligne[:-1]))
    fichier.close()
    


def affiche_cases(plateau):
    ...


def main():
    """ Utilisation du sys."""
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "niveau")
        sys.exit(1)
    print(jeu(sys.argv[1]))
    
if __name__ == "__main__":
    main()