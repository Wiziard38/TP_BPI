#!/usr/bin/env python3
import random
import collections
import math
Point = collections.namedtuple("Point", "x y")

def main():
    """ Programme principal pour tracer l'image. """

    def distance2(centre, x, y):
        """ Calcul la distance d'un point, de coords x et y a un centre de cercle. """
        return (x - centre.x)**2 + (y - centre.y)**2

    # Les trois premieres lignes d'en-tete
    image = open('image.PGM', 'w+')
    image.write('P2\n')
    hauteur = int(input("Quelle hauteur d'image voulez vous ? \n > "))
    largeur = int(input("Quelle largeur d'image voulez vous ? \n > "))
    image.write(f"{largeur} {hauteur}\n")
    image.write('255\n')

    # Les coordonnees et tailles de ces deux cercles, aléatoires
    centre1 = Point(random.randint(0, largeur), random.randint(0, hauteur))
    rayon1 = random.randint(0, min(centre1.x, largeur - centre1.x, centre1.y, hauteur - centre1.y))**2
    centre2 = Point(random.randint(0, largeur), random.randint(0, hauteur))
    rayon2 = random.randint(0, min(centre2.x, largeur - centre2.x, centre2.y, hauteur - centre2.y))**2

    # Tracé de tous les pixels
    for y in range(hauteur):
        for x in range(largeur):
            if distance2(centre1, x, y) > rayon1 and distance2(centre2, x, y) > rayon2:
                image.write("255 ")
            else:
                image.write(str(random.randint(0,255)) + " ")
        image.write("\n")
    
if __name__ == "__main__":
    main()