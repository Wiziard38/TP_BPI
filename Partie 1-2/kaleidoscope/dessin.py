#!/usr/bin/env python3

import random
import svg

def couleur_aleatoire():
    """
    Fonction qui va renvoyer une couleur aleatoire, au format RGB lisible par SVG.
    """
    return f"rgb{tuple(random.sample(range(0,255), 3))}"


def affiche_triangle(triangle_tourne, couleur):
    """
    Fonction qui va appeler le module svg pour afficher les triangles avec une couleur donnee.
    """
    
    print(svg.genere_polygone(triangle_tourne, couleur))