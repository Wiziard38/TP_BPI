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

    plateau_vide = creer_plateau_vide(plateau)
    affiche_plateau(plateau)

    nb_coups = 0
    while plateau != plateau_vide:
        affiche_plateau(plateau)
        nb_coups += 1
        while 1:
            case = input('Choisissez une case a jouer : \n > ')
            if case[1].isnumeric():
                x = int(case[1]) - 1
            else: 
                x = -1
            y = ord(case[0]) - 65
            if 0 <= x < len(plateau) and 0 <= y < len(plateau[0]):
                break
            print('Case non valide !')
        plateau = changement_light(plateau, x, y)
    
    affiche_plateau(plateau)
    print(f"Felicitations, vous avez resolu le niveau en {nb_coups} coups")


def changement_light(plateau, x, y):
    """
    Fonction qui va modifier le plateau accordement au coup joué.
    """

    # La case
    if plateau[y][x] == '_':
        plateau[y][x] = '.'
    else:
        plateau[y][x] = '_'

    # Case en haut
    if y > 0:
        if plateau[y-1][x] == '_':
            plateau[y-1][x] = '.'
        else:
            plateau[y-1][x] = '_'
    
    # Case a gauche
    if x > 0:
        if plateau[y][x-1] == '_':
            plateau[y][x-1] = '.'
        else:
            plateau[y][x-1] = '_'

    # Case en bas
    if y < len(plateau) - 1:
        if plateau[y+1][x] == '_':
            plateau[y+1][x] = '.'
        else:
            plateau[y+1][x] = '_'
    
    # Case a droite
    if x < len(plateau[0]) - 1:
        if plateau[y][x+1] == '_':
            plateau[y][x+1] = '.'
        else:
            plateau[y][x+1] = '_'

    return plateau


def creer_plateau_vide(plateau):
    """
    Fonction qui va creer un plateau vide de meme dimension pour savoir quand une
    partie sera terminee.
    """

    plateau_vide = []
    h = len(plateau)
    l = len(plateau[0])
    for _ in range(h):
        plateau_vide.append(['_']*l)
    return plateau_vide


def affiche_plateau(plateau):
    """
    Fonction qui va afficher le plateau dans le terminal.
    """
    h = len(plateau)
    l = len(plateau[0])
    import os

    os.system('clear')
    # Premiere ligne
    print('    ', end = '')
    for i in range(l):
        print(f'  {i+1}  ', end = '')
    print('\n   ', end = '')
    print('+' + '-----'*l + '+')

    # Lignes centrales
    for i in range(h):
        for x in range(3):
            if x == 1:
                print(f'{chr(65 + i)}  |', end = '')
            else:
                print('   |', end = '')

            for k in range(l):
                if plateau[i][k] == '_':
                    print('     ', end = '')
                else:
                    print('\x1b[0;47;47m' + '     ' + '\x1b[0m', end = '')
            print('|')
    
    # Derniere ligne
    print('   +' + '-----'*l + '+')


def main():
    """ Utilisation du sys."""
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "niveau")
        sys.exit(1)

    jeu(sys.argv[1])
    
if __name__ == "__main__":
    main()