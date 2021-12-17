#!/usr/bin/env python3

"""
Fichier python qui va générer récursivement un labyrithe et l'afficher sous
format d'une image svg.
"""

from random import randint

import svg

def genere_labyrinthe(entree, sortie, taille_case, image):
    """ Fonction qui trace le labyrinthe en appelant une fonction récursive"""

    if sortie[0] - entree[0] <= taille_case and sortie[1] - entree[1] <= taille_case:
        return

    # On regarde si le rectangle est plus en largeur ou en hauteur
    if sortie[0] - entree[0] > sortie[1] - entree[1]: # Largeur
        position_barre = randint(entree[0] // taille_case + 1, sortie[0] // taille_case) * taille_case
        position_porte = randint(entree[1] // taille_case, sortie[1] // taille_case) * taille_case
        porte = [position_barre, position_porte, 'vertical']
        print(svg.genere_segment(svg.Point(position_barre, entree[1]), svg.Point(position_barre, porte[1])), file = image)
        print(svg.genere_segment(svg.Point(position_barre, porte[1]+taille_case), svg.Point(position_barre, sortie[1])), file = image)
    else: # Hauteur
        position_barre = randint(entree[1] // taille_case + 1, sortie[1] // taille_case) * taille_case
        position_porte = randint(entree[0] // taille_case, sortie[0] // taille_case) * taille_case
        porte = [position_porte, position_barre, 'horizontal']
        print(svg.genere_segment(svg.Point(entree[0], position_barre), svg.Point(porte[0], position_barre)), file = image)
        print(svg.genere_segment(svg.Point(porte[0]+taille_case, position_barre), svg.Point(sortie[0], position_barre)), file = image)

    genere_labyrinthe(entree, porte, taille_case, image)
    genere_labyrinthe(porte, sortie, taille_case, image)

def main():
    """ Fonction qui gère l'ouverture de l'image et l'appel à la fonction
    de création du labyrinthe. """
    # initialisation
    image = open("labyrinthe.svg", 'w')
    nb_cases_largeur = 60
    nb_cases_hauteur = 40
    taille_case = 10

    print(svg.genere_balise_debut_image(taille_case * nb_cases_largeur, taille_case * \
        nb_cases_hauteur), file = image)

    # Font blanc
    print(svg.genere_balise_debut_groupe('white', 'white', 0), file = image)
    print(svg.genere_rectangle(svg.Point(0, 0), nb_cases_largeur*taille_case, nb_cases_hauteur*taille_case), file = image)
    print(svg.genere_balise_fin_groupe(), file = image)

    # Labyrinthe
    print(svg.genere_balise_debut_groupe('black', None, 3), file = image)
    print(svg.genere_rectangle(svg.Point(0, 0), nb_cases_largeur*taille_case, nb_cases_hauteur*taille_case), file = image)

    genere_labyrinthe([0, 0, 'horizontal'], \
        [taille_case * nb_cases_largeur, taille_case * nb_cases_hauteur, 'horinzontal'], \
        taille_case, image)

    print(svg.genere_balise_fin_groupe(), file = image)
    print(svg.genere_balise_fin_image(), file = image)


if __name__ == '__main__':
    main()
