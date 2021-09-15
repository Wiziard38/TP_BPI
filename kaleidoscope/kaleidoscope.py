#!/usr/bin/env python3
"""Kaleidoscope.

Exercice graphique, quelques boucles, deux modules à écrire.
"""
import sys
from math import pi

sys.path.append('C:\\Users\mathi\OneDrive\Documents\TP_BPI\SVG')

import dessin
import svg
import triangle 

def genere_image(nombre_triangles):
    """Génère le nombre de triangles demandé aleatoirement, les tourne.

    Affiche le SVG correspondant sur la sortie standard.
    """

    transparence = 0.6
    largeur, hauteur = 800.0, 600.0
    print(svg.genere_balise_debut_image(largeur, hauteur))
    print(svg.genere_balise_debut_groupe_transp(transparence))
    
    centre = svg.Point(largeur / 2, hauteur / 2)

    for _ in range(nombre_triangles):
        # on génère un triangle à l'interieur du quart en bas
        # à droite de l'image.
        triangle_alea = triangle.triangle_aleatoire(
            (largeur / 2, largeur),
            (hauteur / 2, hauteur)
        )
        couleur = dessin.couleur_aleatoire()

        # on tourne et on affiche 8 fois le triangle
        for tour in range(8):
            angle = pi / 4 * tour
            triangle_tourne = triangle.tourne_triangle_autour(triangle_alea, centre, angle)
            dessin.affiche_triangle(triangle_tourne, couleur)

    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())


def main():
    """On génère un SVG kaléidoscopique à partir d'un nombre de triangles"""
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "nombre_triangles > image.svg")
        sys.exit(1)

    nombre_triangles = int(sys.argv[1])
    genere_image(nombre_triangles)


if __name__ == "__main__":
    main()