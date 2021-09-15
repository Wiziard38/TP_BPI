#!/usr/bin/env python3

#import sys
import collections
#sys.path.append("/Users/mathis/Desktop/TP_BPI/SVG") # Import file different folder
import svg
Point = collections.namedtuple('Point', 'x y')

def main():
    print(svg.genere_balise_debut_image(640,480))
    print(svg.genere_balise_debut_groupe("black", 'black', 1))

    for x in range(1000):
        x = input()
        y = input()
        point = Point(x,y)
        print(svg.genere_cercle(point, 1))

    print(svg.genere_balise_fin_groupe())
    print(svg.genere_balise_fin_image())

if __name__ == '__main__':
    main()