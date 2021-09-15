#!/usr/bin/env python 

from svg import *
import collections
import os
os.chdir("/Users/mathis/Desktop/TP_BPI")
Point = collections.namedtuple("Point", "x, y")

def trace_image():
    image = open('mon_image.svg', 'w+')
    
    # Dimensions de l'image
    hauteur = int(input("Quelle hauteur de l'image ? \n > "))
    largeur = int(input("Quelle largeur de l'image ? \n > "))
    image.write(genere_balise_debut_image(largeur, hauteur))

    # Choix a dessiner
    # choix = ''
    # while choix != 'x':

        # choix = input("Que voulez vous dessiner ?   \n - Une ligne (l) \
        #                                             \n - Un cercle (c) \
        #                                             \n - Un groupe de formes (g) \
        #                                             \n - Une figure en avancant / tournant (f) \
        #                                             \n - Arreter (x) \
        #                                             \n > ")
        

    couleur_ligne = input("Quelle couleur de ligne ?")
    couleur_rempli = input("Quelle couleur de remplissage ?")
    epaiss_ligne = input("Quelle epaisseur de ligne ?")
    image.write("\t")
    image.write(genere_balise_debut_groupe(couleur_ligne, couleur_rempli, epaiss_ligne))

    nb_cercles = int(input("Combien de cercles ?"))
    for _ in range(nb_cercles):
        rayon = int(input("Quel rayon du cercle ?"))
        x = int(input("abscisse du centre ?"))
        y = int(input("ordonnee du centre ?"))
        centre = Point(x, y)
        image.write("\t\t")
        image.write(genere_cercle(centre, rayon))
    
    image.write("\t")
    image.write(genere_balise_fin_groupe())
    image.write(genere_balise_fin_image())
    
    image.close()

trace_image()