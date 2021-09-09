"""Module tortue logo.

Ce module implémente les primitives graphiques basiques
d'une tortue logo.
"""

import svg
import math
from collections import namedtuple
Point = namedtuple('Point', 'x y')

def avance(abscisse, ordonnee, direction, crayon_en_bas, distance):
    """Fait avancer la tortue.

    Fait avancer la tortue dans la direction donnée et de la distance donnée.
    Affiche le segment SVG correspondant sur la sortie standard
    si le crayon est en bas.

    Renvoie la nouvelle position de la tortue sous la forme
    d'un Point (défini dans notre module svg).
    """
    
    abscisse_arrivee = abscisse + math.cos(math.radians(direction))*distance
    ordonnee_arrivee = ordonnee - math.sin(math.radians(direction))*distance

    if crayon_en_bas: # On trace la ligne si le crayon est descendu
        dep = Point(abscisse, ordonnee)
        arr = Point(abscisse_arrivee, ordonnee_arrivee)
        print(svg.genere_segment(dep, arr))
    return (abscisse_arrivee, ordonnee_arrivee)

def tourne_droite(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    
    return (direction - angle)%360

def tourne_gauche(direction, angle):
    """
    Fait tourner la tortue à droite.

    Fait tourner la tortue à partir de direction en tournant
    à droite de l'angle donné (en degrés).

    Renvoie la nouvelle direction.
    """
    
    return (direction + angle)%360