#!/usr/env/bin/python3

import collections

Point = collections.namedtuple("Point", "x, y")
Triangle = collections.namedtuple("Triangle", "p1, p2, p3")

point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = Point(-1, 1)
tri = Triangle(point1, point2, point3)

def affiche_tri(tri):
    """ Affichache des coordonnees d'un triangle"""
    print("coordonnees du triangle : (" + str(tri.p1.x) + ";" + str(tri.p1.y) + ") (" 
        + str(tri.p2.x) + ";" + str(tri.p2.y) + ") (" 
        + str(tri.p3.x) + ";" + str(tri.p3.y) + ").")
