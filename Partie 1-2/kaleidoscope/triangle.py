#!/usr/bin/env python3

import random
import svg
import math

def triangle_aleatoire(bornes_abscisses, bornes_hauteur):
    """
    Fonction qui genere aleatoirement un triangle appartenant a une partie du plan definie en parametre.
    """

    point1 = svg.Point(random.randint(bornes_abscisses[0], bornes_abscisses[1]), random.randint(bornes_hauteur[0], bornes_hauteur[1]))
    point2 = svg.Point(random.randint(bornes_abscisses[0], bornes_abscisses[1]), random.randint(bornes_hauteur[0], bornes_hauteur[1]))
    point3 = svg.Point(random.randint(bornes_abscisses[0], bornes_abscisses[1]), random.randint(bornes_hauteur[0], bornes_hauteur[1]))
    return (point1, point2, point3)


def tourne_triangle_autour(triangle, centre, angle):
    """
    FOnction qui renvoie un meme triangle que en parametre, mais tourne d'un certain angle par rapport a un point (centre).
    """

    point1, point2, point3 = triangle
    # Point 1
    x = (point1.x - centre.x)*math.cos(angle) - (point1.y - centre.y)*math.sin(angle) + centre.x
    y = (point1.x - centre.x)*math.sin(angle) + (point1.y - centre.y)*math.cos(angle) + centre.y
    point1 = svg.Point(x, y)
    # Point 2
    x = (point2.x - centre.x)*math.cos(angle) - (point2.y - centre.y)*math.sin(angle) + centre.x
    y = (point2.x - centre.x)*math.sin(angle) + (point2.y - centre.y)*math.cos(angle) + centre.y
    point2 = svg.Point(x, y)
    # Point 3
    x = (point3.x - centre.x)*math.cos(angle) - (point3.y - centre.y)*math.sin(angle) + centre.x
    y = (point3.x - centre.x)*math.sin(angle) + (point3.y - centre.y)*math.cos(angle) + centre.y
    point3 = svg.Point(x, y)
    return (point1, point2, point3)