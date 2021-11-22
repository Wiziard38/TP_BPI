#!/usr/bin/env python3

"""Listes simplement chaînées, triées, circulaires et avec sentinelle."""

import traceur

class Cellule:
    """ Une cellule d'une liste simplement chaînée.
    Possède une référence vers la valeur et
    une référence vers la cellule suivante.
    """
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        return "cellule_" + str(self.valeur)


class ListeSimplementChaineeTriee:
    """Listes simplement chaînées, triées, circulaires et avec sentinelle."""

    def __init__(self, sentinelle, nombres=None):
        """Construit la liste avec le range de nombres donné.

        `sentinelle` precise la valeur de la cellule sentinelle.
        pre-condition: le range de nombres donné est trié si il est
                       différent de None.
        Si le range est différent de None, on créera directement les cellules
        ici dans le constructeur. Autrement dit, on n'utilisera pas la fonction
        ajoute.
        """

        self.tete = Cellule(sentinelle, None)
        cellule_courante = self.tete
        if nombres:
            for indice, valeur in enumerate(nombres):
                cellule_suivante = Cellule(valeur, None)
                cellule_courante.suivant = cellule_suivante
                cellule_courante = cellule_suivante
            cellule_courante.suivant = self.tete

    def __str__(self):
        """Renvoie la chaîne de caractères "val1 --> val2 --> val3 ..." """
        cellule_courante = self.tete
        sentinelle = cellule_courante.valeur
        cellule_courante = cellule_courante.suivant
        if cellule_courante.valeur == sentinelle:
            return ''
        chaine = f'{cellule_courante.valeur}'
        while cellule_courante.suivant.valeur != sentinelle:
            cellule_courante = cellule_courante.suivant
            chaine += f' --> {cellule_courante.valeur}'
        return chaine


def ajoute(liste_chainee, valeur):
    """Ajoute la valeur donnée à la bonne place dans la liste chaînée.

    pre-condition : `valeur` n'est pas la valeur de la sentinelle.
    """
    sentinelle = liste_chainee.tete.valeur
    cellule_courante = liste_chainee.tete
    while cellule_courante.suivant.valeur < valeur and cellule_courante.suivant.valeur != sentinelle:
        cellule_courante = cellule_courante.suivant
    if cellule_courante.suivant.valeur == sentinelle:
        cellule_courante.suivant = Cellule(valeur, liste_chainee.tete)
    else:
        cellule_suivante = cellule_courante.suivant
        cellule_courante.suivant = Cellule(valeur, cellule_suivante)

def supprime(liste_chainee, valeur):
    """Supprime la première cellule de la liste chaînée avec la valeur donnée.

    pre-condition : `valeur` n'est pas la valeur de la sentinelle.
    """
    sentinelle = liste_chainee.tete.valeur
    cellule_courante = liste_chainee.tete
    while cellule_courante.suivant.valeur != valeur and cellule_courante.suivant.valeur != sentinelle:
        cellule_courante = cellule_courante.suivant
    if cellule_courante.suivant.valeur != sentinelle:
        cellule_courante.suivant = cellule_courante.suivant.suivant


def decoupe(liste_chainee):
    """Découpe la liste chaînée en deux, une cellule sur 2.

    Par exemple (1,2,3,4,5) produit (1,3,5) et (2,4).
    Renvoie les deux nouvelles listes.
    Aucune nouvelle cellule n'est créée hormis les sentinelles
    des deux nouvelles listes.
    En sortie `liste_chainee` est vide.
    """
    sentinelle = liste_chainee.tete.valeur

    liste_chainee_1 = ListeSimplementChaineeTriee(sentinelle)
    cellule_courante_1 = liste_chainee_1.tete
    liste_chainee_2 = ListeSimplementChaineeTriee(sentinelle)
    cellule_courante_2 = liste_chainee_2.tete

    flag = True
    cellule_courante = liste_chainee.tete.suivant
    while cellule_courante.suivant.valeur != sentinelle:
        if flag:
            cellule_courante_1.suivant = cellule_courante
            cellule_courante_1 = cellule_courante
            flag = False
        else:
            cellule_courante_2.suivant = cellule_courante
            cellule_courante_2 = cellule_courante
            flag = True
        cellule_courante = cellule_courante.suivant
        liste_chainee.tete.suivant = cellule_courante

    if flag:
        cellule_courante_1.suivant = cellule_courante
        cellule_courante_1 = cellule_courante
    else:
        cellule_courante_2.suivant = cellule_courante
        cellule_courante_2 = cellule_courante

    cellule_courante_1.suivant = liste_chainee_1.tete
    cellule_courante_2.suivant = liste_chainee_2.tete
    liste_chainee.tete.suivant = liste_chainee.tete

    return liste_chainee_1, liste_chainee_2

def test():
    """Tests simples des différentes fonctions (à compléter)"""

    # On crée une liste simplement chaînée triée circulaire et l'on affiche
    liste_chainee = ListeSimplementChaineeTriee(float("inf"), range(1, 6))

    liste_chainee_variable = traceur.Variable('liste_chainee', liste_chainee)
    traceur.display_vars(liste_chainee_variable, visualize=False,
                         image_name="liste_chainee_0_a_7")

    print("liste_chainee :", liste_chainee)


    # On ajoute et on supprime puis on affiche
    ajoute(liste_chainee, 0)
    ajoute(liste_chainee, 7)
    ajoute(liste_chainee, 6)
    ajoute(liste_chainee, 5)
    supprime(liste_chainee, 5)
    ajoute(liste_chainee, 8)
    supprime(liste_chainee, 8)
    print("liste_chainee :", liste_chainee)

    # On trace notre liste
    liste_chainee_variable = traceur.Variable('liste_chainee', liste_chainee)
    traceur.display_vars(liste_chainee_variable, visualize=False,
                         image_name="liste_chainee_0_a_7")

    # On découpe notre liste
    resultat_decoupe = decoupe(liste_chainee)
    pairs, impairs = resultat_decoupe # ce qu'on fait ici s'appelle du unpacking

    # On trace le résultat de la découpe
    resultat_decoupe_variable = traceur.Variable('res_decoupe', resultat_decoupe)
    traceur.display_vars(resultat_decoupe_variable, visualize=False,
                         image_name="resultat_decoupe")

    # On affiche
    print("pairs   :", pairs)
    print("impairs :", impairs)
    print("liste_chainee :", liste_chainee)

    # On refait quelques suppressions et ajouts pour le plaisir
    # puis on affiche
    supprime(pairs, 4)
    supprime(pairs, 0)
    supprime(pairs, 2)
    supprime(pairs, 6)
    ajoute(impairs, 6)
    ajoute(impairs, 0)
    print("impairs après ajout de 6 et 0 :", impairs)
    print("pairs après suppression de tous les éléments :", pairs)

if __name__ == "__main__":
    test()
