#!/usr/bin/env python3
""" Module python permettant le tracé d'un arbre en SVG. """

from random import randint, random
from math import sqrt, cos, sin, pi

import svg

def distance(point1, point2):
    """ Fonction qui renvoie la distance carthésienne. """
    return (point1.x - point2.x)**2 + (point1.y - point2.y)**2

def deplacement(point, angle, longueur):
    """ Fonction qui translate un point dans l'espace. """
    return svg.Point(point.x + sin(angle)*longueur, point.y - cos(angle)*longueur)

def genere_branche(point_depart, point_arrivee, taille_limite, image):
    """ Fonction recursive qui s'occupe de la génération des branches d'un arbre. """
    taille_branche = sqrt(distance(point_depart, point_arrivee))
    if taille_branche > taille_limite:
        print(svg.genere_segment(point_depart, point_arrivee), file = image)
        nb_branches = randint(2, 4)
        for _ in range(nb_branches):
            angle = (random()-0.5)*pi # Un angle entre -pi et pi
            longueur = random()*taille_branche
            genere_branche(point_arrivee, deplacement(point_arrivee, angle, longueur), \
                taille_limite, image)

def main():
    """ Fonction centrale qui va gérer la création de l'arbre. """
    image = open('arbre.svg', 'w+')
    print(svg.genere_balise_debut_image(800, 600), file = image)
    # Fond de l'image noir
    print(svg.genere_balise_debut_groupe('black', 'black', 1), file = image)
    print(svg.genere_rectangle(svg.Point(0,0), 800, 600), file = image)
    print(svg.genere_balise_fin_groupe(), file = image)

    # L'arbre en blanc
    print(svg.genere_balise_debut_groupe('white', 'none', 1), file = image)
    genere_branche(svg.Point(400, 550), svg.Point(400, 350), 5, image)
    print(svg.genere_balise_fin_groupe(), file = image)
    print(svg.genere_balise_fin_image(), file = image)

if __name__ == '__main__':
    main()
