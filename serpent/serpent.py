#!/usr/bin/env python3

import sys
#import numpy as np
sys.path.append('C:\\Users\mathi\OneDrive\Documents\TP_BPI\SVG')
import svg


def genere_image(hauteur, largeur):
    """Génère le jeu du serpent demandé.
    Affiche le SVG correspondant sur la sortie standard.
    """
    taille_case = 40
    print(svg.genere_balise_debut_image(largeur, hauteur))

    # Initialisation
    nb_places_vertical = hauteur // 40
    nb_places_horizontal = largeur // 40
    nombre_lignes = (nb_places_vertical-1)//2 + 1
    nombre_cases = nb_places_horizontal*(nombre_lignes) + nombre_lignes - 1
    
    direction = (nombre_lignes % 2 == 0)
    if direction:
        (x, y) = (0, 0)
    else:
        (x, y) = (largeur - taille_case, 0)

    # Creation
    for i in range(nombre_lignes):
        for k in range(nb_places_horizontal):
            print(creer_carre(x, y, taille_case))
            
            if direction:
                x += taille_case/4
                print(f"<text x={x} y={y+35} fill='red'> {nombre_cases} </text>\n")
                x += taille_case/4*3
                nombre_cases -= 1
            else:
                x += taille_case/4
                print(f"<text x={x} y={y+35} fill='red'> {nombre_cases} </text>\n")
                x -= taille_case/4*5
                nombre_cases -= 1

        if direction and nombre_cases != 0:
            y += taille_case # On descend
            x -= taille_case/4*3 # On revient a gauche
            print(f"<text x={x} y={y+35} fill='red'> {nombre_cases} </text>\n")
            x -= taille_case/4
            print(creer_carre(x, y, taille_case))
            nombre_cases -= 1
        elif not(direction)  and nombre_cases != 0:
            y += taille_case # On descend
            x += taille_case/4*5 # On revient a droite
            print(f"<text x={x} y={y+35} fill='red'> {nombre_cases} </text>\n")
            x -= taille_case/4
            print(creer_carre(x, y, taille_case))
            nombre_cases -= 1
        direction = direction ^ True
        y += taille_case

    print(svg.genere_balise_fin_image())


def creer_carre(x, y, taille):
    """
    Creer in carre de taille donnee a une certaine cordonnee.
    """
    return f"<rect x={x} y={y} width={taille} height={taille} style='fill:none;stroke:black;stroke-width:2'/>\n"


def main():
    """On génère un SVG du jeu du serpent"""
    if len(sys.argv) != 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "hauteur largeur > image.svg")
        sys.exit(1)

    hauteur = int(sys.argv[1])
    largeur = int(sys.argv[2])
    genere_image(hauteur, largeur)


if __name__ == "__main__":
    main()