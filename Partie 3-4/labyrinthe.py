#!/usr/bin/env python3
# pylint: disable=line-too-long

"""
Fichier python qui va générer récursivement un labyrithe et l'afficher sous
format d'une image svg.
"""

from random import randint, seed
seed(12)

import svg

nb_rec = 0

def genere_labyrinthe(top_left, down_right, entree, sortie, taille_case, image, trace = False):
    """ Fonction qui trace le labyrinthe en appelant une fonction récursive"""
    global nb_rec
    nb_rec += 1
    if nb_rec > 52:
        return

    if down_right[0] - top_left[0] <= taille_case and down_right[1] - top_left[1] <= taille_case:
        if trace is False:
            return

        print(svg.genere_balise_debut_groupe('blue', 'none', 3), file = image)
        if entree[0] == entree[2]: # entree verticale
            if entree[0] < max(sortie[0], sortie[2]): # a gauche
                print(svg.genere_segment(svg.Point(entree[0], entree[1] + taille_case/2), \
                    svg.Point(entree[0] + taille_case/2, entree[1] + taille_case/2)), file = image)
            else: # a droite
                print(svg.genere_segment(svg.Point(entree[0] - taille_case/2, entree[1] + taille_case/2), \
                    svg.Point(entree[0], entree[1] + taille_case/2)), file = image)
        else: # entree horizontale
            if entree[1] < max(sortie[1], sortie[2]): # en haut
                print(svg.genere_segment(svg.Point(entree[0] + taille_case/2, entree[1]), \
                    svg.Point(entree[0] + taille_case/2, entree[1] + taille_case/2)), file = image)
            else: # en bas
                print(svg.genere_segment(svg.Point(entree[0] + taille_case/2, entree[1] - taille_case/2), \
                    svg.Point(entree[0] + taille_case/2, entree[1])), file = image)

        if sortie[0] == sortie[2]: # sortie verticale
            if sortie[0] < max(entree[0], entree[2]): # a gauche
                print(svg.genere_segment(svg.Point(sortie[0], sortie[1] + taille_case/2), \
                    svg.Point(sortie[0] + taille_case/2, sortie[1] + taille_case/2)), file = image)
            else: # a droite
                print(svg.genere_segment(svg.Point(sortie[0] - taille_case/2, sortie[1] + taille_case/2), \
                    svg.Point(sortie[0], sortie[1] + taille_case/2)), file = image)
        else: # sortie horizontale
            if sortie[1] < max(entree[1], entree[2]): # en haut
                print(svg.genere_segment(svg.Point(sortie[0] + taille_case/2, sortie[1]), \
                    svg.Point(sortie[0] + taille_case/2, sortie[1] + taille_case/2)), file = image)
            else: # en bas
                print(svg.genere_segment(svg.Point(sortie[0] + taille_case/2, sortie[1] - taille_case/2), \
                    svg.Point(sortie[0] + taille_case/2, sortie[1])), file = image)
        
        print(svg.genere_balise_fin_groupe(), file = image)
        return

    # On regarde si le rectangle est plus en largeur ou en hauteur
    if down_right[0] - top_left[0] > down_right[1] - top_left[1]: # Largeur
        position_barre = randint(top_left[0] // taille_case + 1, down_right[0] // taille_case - 1) * taille_case
        position_porte = randint(top_left[1] // taille_case, down_right[1] // taille_case - 1) * taille_case
        porte = [position_barre, position_porte, position_barre, position_porte + taille_case]

        print(svg.genere_segment(svg.Point(position_barre, top_left[1]), svg.Point(position_barre, porte[1])), file = image)
        print(svg.genere_segment(svg.Point(position_barre, porte[1]+taille_case), svg.Point(position_barre, down_right[1])), file = image)

        # Recursion
        if position_barre > min(entree[0], entree[2], sortie[0], sortie[2]) and trace:
            if position_barre < max(entree[0], entree[2], sortie[0], sortie[2]):
                genere_labyrinthe(top_left, [position_barre, down_right[1]], entree, porte, taille_case, image, trace = True)
            else:
                genere_labyrinthe(top_left, [position_barre, down_right[1]], entree, sortie, taille_case, image, trace = True)
        else:
            genere_labyrinthe(top_left, [position_barre, down_right[1]], entree, porte, taille_case, image)
        
        if position_barre < max(entree[0], entree[2], sortie[0], sortie[2]) and trace:
            if position_barre > min(entree[0], entree[2], sortie[0], sortie[2]):
                genere_labyrinthe([position_barre, top_left[1]], down_right, porte, sortie, taille_case, image, trace = True)
            else:
                genere_labyrinthe([position_barre, top_left[1]], down_right, entree, sortie, taille_case, image, trace = True)
        else:
            genere_labyrinthe([position_barre, top_left[1]], down_right, porte, sortie, taille_case, image)

    else: # Hauteur
        position_barre = randint(top_left[1] // taille_case + 1, down_right[1] // taille_case - 1) * taille_case
        position_porte = randint(top_left[0] // taille_case, down_right[0] // taille_case - 1) * taille_case
        porte = [position_porte, position_barre, position_porte + taille_case, position_barre]

        print(svg.genere_segment(svg.Point(top_left[0], position_barre), svg.Point(porte[0], position_barre)), file = image)
        print(svg.genere_segment(svg.Point(porte[0]+taille_case, position_barre), svg.Point(down_right[0], position_barre)), file = image)

        # Recursion
        if position_barre > min(entree[1], entree[3], sortie[1], sortie[3]) and trace:
            if position_barre < max(entree[1], entree[3], sortie[1], sortie[3]):
                genere_labyrinthe(top_left, [down_right[0], position_barre], entree, porte, taille_case, image, trace = True)
            else:
                genere_labyrinthe(top_left, [down_right[0], position_barre], entree, sortie, taille_case, image, trace = True)
        else:
            genere_labyrinthe(top_left, [down_right[0], position_barre], entree, porte, taille_case, image)

        if position_barre < max(entree[1], entree[3], sortie[1], sortie[3]) and trace:
            if position_barre > min(entree[1], entree[3], sortie[1], sortie[3]):
                genere_labyrinthe([top_left[0], position_barre], down_right, porte, sortie, taille_case, image, trace = True)
            else:
                genere_labyrinthe([top_left[0], position_barre], down_right, entree, sortie, taille_case, image, trace = True)
        else:
            genere_labyrinthe([top_left[0], position_barre], down_right, porte, sortie, taille_case, image)

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

    # Contour
    print(svg.genere_balise_debut_groupe('black', None, 5), file = image)
    print(svg.genere_rectangle(svg.Point(0, 0), 600, 400), file = image)
    print(svg.genere_balise_fin_groupe(), file = image)
    print(svg.genere_balise_debut_groupe('white', 'white', 0), file = image)
    print(svg.genere_rectangle(svg.Point(2.5, 0), 7.5, 10), file = image)
    print(svg.genere_rectangle(svg.Point(587.5, 390), 10, 10), file = image)
    print(svg.genere_balise_fin_groupe(), file = image)

    # Labyrinthe
    print(svg.genere_balise_debut_groupe('black', None, 3), file = image)
    genere_labyrinthe([0, 0], [600, 400], [0, 0, 10, 0], [590, 400, 600, 400], taille_case, image, trace = True)
    print(svg.genere_balise_fin_groupe(), file = image)

    print(svg.genere_balise_fin_image(), file = image)


if __name__ == '__main__':
    main()
