#!/usr/bin/env python3

import svg
import sys
from collections import namedtuple
Point = namedtuple("Point", "x, y")

def affichage():
    """Programme qui va gerer l'affichage sur la sortie standard"""
    print(svg.genere_balise_debut_image(800, 800))
    for x in range(0, 800, 100):
        for y in range(0, 800, 100):
            if ((x+y)/100)%2 == 0:
                print(svg.genere_balise_debut_groupe(None, 'Black', 0))
            else:
                print(svg.genere_balise_debut_groupe(None, 'White', 0))
            print(svg.genere_rectangle(Point(x, y), 100, 100))
            print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_debut_groupe('Red', None, 10))
    print(svg.genere_rectangle(Point(1,1), 798, 798))
    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())


def main():
    """
    Programme principal qui va gerer l'affichage de l'echiquier.
    """
    
    # if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
    #     print("utilisation:", sys.argv[0], " > image.svg")
    #     sys.exit(1)

    affichage()

if __name__ == '__main__':
    main()