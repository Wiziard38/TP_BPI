#!/usr/bin/env python3
# pylint: disable=line-too-long

"""
Fichier python qui va générer récursivement un labyrithe et l'afficher sous
format d'une image svg.
"""

from random import randint
import svg


def genere_labyrinthe(top_left, down_right, entree, sortie, taille_case, image, trace = False):
    """ Fonction qui trace le labyrinthe en appelant une fonction récursive"""

    if down_right[0] - top_left[0] <= taille_case and down_right[1] - top_left[1] <= taille_case:
        if trace is False:
            return

        print(svg.genere_balise_debut_groupe('red', 'none', 3), file = image)
        entree_sortie = set()
        if entree[0] == entree[2]: # entree verticale
            if sortie[0] == sortie[2]:
                entree_sortie = {'droite', 'gauche'}
            else: # sortie horizontale
                if entree[0] < max(sortie[0], sortie[2]):
                    entree_sortie.add('gauche')
                else:
                    entree_sortie.add('droite')
                if sortie[1] < max(entree[1], entree[3]):
                    entree_sortie.add('haut')
                else:
                    entree_sortie.add('bas')
        else: # entree horizontale
            if sortie[1] == sortie[3]:
                entree_sortie = {'bas', 'haut'}
            else: # sortie verticale
                if entree[1] < max(sortie[1], sortie[3]):
                    entree_sortie.add('haut')
                else:
                    entree_sortie.add('bas')
                if sortie[0] < max(entree[0], entree[2]):
                    entree_sortie.add('gauche')
                else:
                    entree_sortie.add('droite')

        haut_gauche = [min(entree[0], sortie[0]), min([entree[1], sortie[1]])]
        if 'haut' in entree_sortie:
            print(svg.genere_segment(svg.Point(haut_gauche[0] + taille_case/2, haut_gauche[1]), \
                    svg.Point(haut_gauche[0] + taille_case/2, haut_gauche[1] + taille_case/2)), file = image)
        if 'bas' in entree_sortie:
            print(svg.genere_segment(svg.Point(haut_gauche[0] + taille_case/2, haut_gauche[1] + taille_case/2), \
                    svg.Point(haut_gauche[0] + taille_case/2, haut_gauche[1] + taille_case)), file = image)
        if 'droite' in entree_sortie:
            print(svg.genere_segment(svg.Point(haut_gauche[0] + taille_case/2, haut_gauche[1] + taille_case/2), \
                    svg.Point(haut_gauche[0] + taille_case, haut_gauche[1] + taille_case/2)), file = image)
        if 'gauche' in entree_sortie:
            print(svg.genere_segment(svg.Point(haut_gauche[0], haut_gauche[1] + taille_case/2), \
                    svg.Point(haut_gauche[0] + taille_case/2, haut_gauche[1] + taille_case/2)), file = image)

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
        if trace is False:
            genere_labyrinthe(top_left, [position_barre, down_right[1]], [], [], taille_case, image)
            genere_labyrinthe([position_barre, top_left[1]], down_right, [], [], taille_case, image)
        else:
            if entree[0] > sortie[0]:
                (entree, sortie) = (sortie, entree)
            if position_barre > min(entree[0], entree[2], sortie[0], sortie[2]):
                if position_barre < max(entree[0], entree[2], sortie[0], sortie[2]):
                    genere_labyrinthe(top_left, [position_barre, down_right[1]], entree, porte, taille_case, image, trace = True)
                    genere_labyrinthe([position_barre, top_left[1]], down_right, porte, sortie, taille_case, image, trace = True)
                else:
                    genere_labyrinthe(top_left, [position_barre, down_right[1]], entree, sortie, taille_case, image, trace = True)
                    genere_labyrinthe([position_barre, top_left[1]], down_right, [], [], taille_case, image)
            else:
                genere_labyrinthe(top_left, [position_barre, down_right[1]], [], [], taille_case, image)
                genere_labyrinthe([position_barre, top_left[1]], down_right, entree, sortie, taille_case, image, trace = True)

    else: # Hauteur
        position_barre = randint(top_left[1] // taille_case + 1, down_right[1] // taille_case - 1) * taille_case
        position_porte = randint(top_left[0] // taille_case, down_right[0] // taille_case - 1) * taille_case
        porte = [position_porte, position_barre, position_porte + taille_case, position_barre]

        print(svg.genere_segment(svg.Point(top_left[0], position_barre), svg.Point(porte[0], position_barre)), file = image)
        print(svg.genere_segment(svg.Point(porte[0]+taille_case, position_barre), svg.Point(down_right[0], position_barre)), file = image)

        # Recursion
        if trace is False:
            genere_labyrinthe(top_left, [down_right[0], position_barre], [], [], taille_case, image)
            genere_labyrinthe([top_left[0], position_barre], down_right, [], [], taille_case, image)
        else:
            if entree[1] > sortie[1]:
                (entree, sortie) = (sortie, entree)
            if position_barre > min(entree[1], entree[3], sortie[1], sortie[3]):
                if position_barre < max(entree[1], entree[3], sortie[1], sortie[3]):
                    genere_labyrinthe(top_left, [down_right[0], position_barre], entree, porte, taille_case, image, trace = True)
                    genere_labyrinthe([top_left[0], position_barre], down_right, porte, sortie, taille_case, image, trace = True)
                else:
                    genere_labyrinthe(top_left, [down_right[0], position_barre], entree, sortie, taille_case, image, trace = True)
                    genere_labyrinthe([top_left[0], position_barre], down_right, [], [], taille_case, image)
            else:
                genere_labyrinthe(top_left, [down_right[0], position_barre], [], [], taille_case, image)
                genere_labyrinthe([top_left[0], position_barre], down_right, entree, sortie, taille_case, image, trace = True)


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
