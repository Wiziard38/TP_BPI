#!/usr/bin/env python3
""" Module python permettant le tracé d'un arbre en SVG. """

from random import randint, random
from math import sqrt, cos, sin, pi, atan

import svg

def distance(point1, point2):
    """ Fonction qui renvoie la distance carthésienne. """
    return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def deplacement(point, angle, longueur):
    """ Fonction qui translate un point dans l'espace. """
    return svg.Point(point.x + cos(angle)*longueur, point.y - sin(angle)*longueur)

def recup_angle(point1, point2):
    """ Fonction qui renvoie l'angle entre 2 points et la verticale. """
    if point1.x == point2.x:
        return pi/2
    if point1.x < point2.x:
        return atan((point1.y - point2.y)/(point2.x - point1.x))
    return pi - atan((point1.y - point2.y)/(point1.x - point2.x))

def genere_branche(point_depart, point_arrivee, taille_limite, image):
    """ Fonction recursive qui s'occupe de la génération des branches d'un arbre. """
    taille_branche = distance(point_depart, point_arrivee)
    if taille_branche < taille_limite:
        return
    if point_arrivee.y < 50 or point_arrivee.x < 50 or point_arrivee.x > 750:
        return

    print(svg.genere_segment(point_depart, point_arrivee), file = image)
    nb_branches = randint(2, 4)
    for _ in range(nb_branches):
        ancien_angle = recup_angle(point_depart, point_arrivee)
        nouveau_depart = deplacement(point_depart, ancien_angle, (1-random()/3)*taille_branche)
        nouvel_angle = (random()-0.5)*2/3*pi + ancien_angle
        longueur = random()*taille_branche
        nouvelle_arrivee = deplacement(nouveau_depart, nouvel_angle, longueur)
        genere_branche(nouveau_depart, nouvelle_arrivee, taille_limite, image)

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
