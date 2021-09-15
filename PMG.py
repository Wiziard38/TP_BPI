#!/usr/bin/env python3
import random
import collections
Point = collections.namedtuple("Point", "x y")

def main():
    """ Programme principal pour tracer l'image. """

    # Les trois premieres lignes d'en-tete
    image = open('image.PGM', 'w+')
    image.write('P2\n')
    hauteur = int(input("Quelle hauteur d'image voulez vous ? \n > "))
    largeur = int(input("Quelle largeur d'image voulez vous ? \n > "))
    image.write(f"{largeur} {hauteur}\n")
    image.write('255\n')

    # Les coordonnees et tailles de ces deux cercles, aléatoires
    centre1 = Point(random.randint(0, largeur), random.randint(0, hauteur))
    rayon1 = random.randint(0, min(centre1.x, largeur - centre1.x, centre1.y, hauteur - centre1.y))
    centre2 = Point(random.randint(0, largeur), random.randint(0, hauteur))
    rayon2 = random.randint(0, min(centre2.x, largeur - centre2.x, centre2.y, hauteur - centre2.y))

    
