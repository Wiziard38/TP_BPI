#!/usr/bin/env python3
"""
On fait une analyse de texte pour dessiner le graphe des mots suivants.
Permet l'utilisation de dictionnaires et une imbrication de structures.
On se sert des donnees pour generer des phrases aleatoires.
"""
import sys
from re import finditer
from random import choice, random, choices
from os import system, chdir
from collections import defaultdict
from copy import deepcopy
chdir("/Users/mathis/Desktop/TP_BPI/mots_suivants")


def get_mots(nom_fichier):
    """Renvoie un tableau dynamique sur tous les mots du fichier.

    Elimine au passage tout ce qui n'est pas une lettre.
    """
    mots = []
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            for mot in finditer("[a-zA-Z]+", ligne):
                mots.append(mot.group(0))
    return mots


def get_couples(tableau):
    """Renvoie un un tableau dynamique des couples.

    Le tableau dynamique renvoyé contient tous les couples d'elements
    successifs de l'iterateur donne.
    """
    couples = []
    valeur_precedente = tableau[0]
    for valeur in tableau[1:]:
        couples.append((valeur_precedente, valeur))
        valeur_precedente = valeur
    return couples


def analyse_texte():
    """Analyse le fichier donné en argument.

    L'analyse parcours les mots du fichier et dessine le graphe
    des mots suivants.

    Ensuite, une phrase aléatoire est générée à partir du dictionnaire
    des mots.
    """

    # Parcours
    if len(sys.argv) != 2:
        print("utilisation :", sys.argv[0], "fichier_texte")
        sys.exit(1)
    suivants = compte_mots_suivants(sys.argv[1])
    genere_graphe(deepcopy(suivants))

    # Génération d'une petite phrase aleatoire.
    mot_depart = str(choice(list(suivants.keys())))
    phrase = [mot_depart]
    for _ in range(10):
        phrase.append(get_suivant_aleatoire(phrase[-1], suivants))
    print(" ".join(phrase))


def compte_mots_suivants(nom_fichier):
    """ Renvoie le dictionnaire des mots suivants.

    Renvoie un dictionnaire associant a chaque mot m1 du fichier
    un dictionnaire associant a chaque mot m2 suivant m1 dans le
    fichier le nombre de fois ou m2 apparait apres m1.
    """
    dict_mots = {}

    liste_mots = get_mots(nom_fichier)
    for mot in liste_mots:
        dict_mots[mot] = defaultdict(int)
    couples = get_couples(liste_mots)
    for couple_mots in couples:
        dict_mots[couple_mots[0]][couple_mots[1]] += 1
    return dict_mots
    

def genere_graphe(suivants):
    """ Genere le graphe dans les fichiers mots-suivants.dot et .png.

    Attention : il faut analyser des petits textes seulement car le
    layout du graph par l'outil dot peut vite coûter très cher en temps
    de calcul.
    """

    # On créer un fichier au format texte dot, utilisé pour
    # décrire un graphe.
    with open("mots-suivants.dot", "w") as fichier_dot:
        fichier_dot.write('digraph { \n')
        while suivants:
            (mot1, dict_suiv) = suivants.popitem()
            while dict_suiv:
                (mot2, occurences) = dict_suiv.popitem()
                fichier_dot.write(f"{mot1} -> {mot2} [label = {occurences}] \n")
        fichier_dot.write('}')

    # On utilise l'outil dot pour convertir le fichier .dot en image
    system("dot -Tpng mots-suivants.dot -o mots-suivants.png")


def get_suivant_aleatoire(mot, suivants):
    """Tire aléatoirement un suivant du mot donné.

    Le tirage aléatoire doit être pondéré par le nombre d'occurrences.
    Si le mot donne n'a pas de suivant, retourne un mot aléatoire.
    """
    if suivants[mot]:
        return choices(list(suivants[mot].keys()), list(suivants[mot].values()))[0]
    return str(choice(list(suivants.keys())))

if __name__ == "__main__":
    analyse_texte()
