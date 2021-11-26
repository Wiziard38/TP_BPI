#!/usr/bin/env python3

""" Listes simplement chainées à partir d'itérateur. """

from cellule import Cellule

class ListeSimplementChainee:
    """Listes simplement chaînées, triées, circulaires et avec sentinelle."""

    def __init__(self, nombres=None):
        """ Construit la liste avec le range de nombres donné. """
        for nombre in nombres:
            if cellule_courante:
                cellule_courante.suivant = Cellule(nombre, None)
                cellule_courante = cellule_courante.suivant
            else:
                self.tete = Cellule(nombre, None)
                cellule_courante = self.tete

    def __str__(self):
        """ Renvoie la chaîne de caractères "val1 --> val2 --> val3 ..." """
        cellule_courante = self.tete
        if cellule_courante.valeur is not None:
            chaine = f'{cellule_courante.valeur}'
        while cellule_courante.suivant.valeur is not None:
            cellule_courante = cellule_courante.suivant
            chaine += f' --> {cellule_courante.valeur}'
        return chaine

def recupere_cellules(liste_chainee):
    """ Fonction génératrice des cellules d'une liste chainee. """
    if liste_chainee.tete is not None:
        cellule_courante = liste_chainee.tete
        yield cellule_courante.valeur
        while cellule_courante.suivant is not None:
            cellule_courante = cellule_courante.suivant
            yield cellule_courante.valeur

def remplace_valeurs(liste_chainee, transforme):
    """ Fonction qui remplace toute les valeur d'une liste chainee selon
    une fonction donnéee. """
    for cellule in recupere_cellules(liste_chainee):
        cellule.valeur = transforme(cellule.valeur)

def filtre_cellules(liste_chainee, filtre):
    """ Fonction génératrice renvoyant True ou False selon le filtre pour une liste donnée """
    for cellule in recupere_cellules(liste_chainee):
        if isinstance(filtre(cellule.valeur), bool):
            raise TypeError
        yield filtre(cellule.valeur)

def supprime_cellules(liste_chainee, filtre):
    """ Fonction qui supprime les cellules d'une liste chainee selon un filtre. """
    iter_filtre = filtre_cellules(liste_chainee, filtre)
    cellule_precedente = None
    for cellule in recupere_cellules(liste_chainee):
        valeur_filtre = next(iter_filtre)
        if not valeur_filtre and cellule_precedente:
            cellule_precedente.suivant = cellule.suivant
        elif not valeur_filtre and not cellule_precedente:
            liste_chainee.tete = cellule.suivant

def concatene(liste_chainee_1, liste_chainee_2):
    """ Fonction qui ajoute les cellules de la liste_chainee_1 à la liste_chainee_2 """
    iter_cellules_1 = recupere_cellules(liste_chainee_1)
    try:
        while True:
            cellule_courante = next(iter_cellules_1)
    except StopIteration:
        pass

    iter_cellules_2 = recupere_cellules(liste_chainee_2)
    for cellule in iter_cellules_2:
        if cellule_courante:
            cellule_courante.suivant = cellule
        else:
            liste_chainee_1.tete = cellule
        cellule_courante = cellule

    liste_chainee_2.tete = None

def decoupe(liste_chainee, fonction):
    """ Fonction qui separe une liste chainee en deux listes selon une fonction. """
    liste_chainee_1 = ListeSimplementChainee()
    cellule_courante_1 = None
    liste_chainee_2 = ListeSimplementChainee()
    cellule_courante_2 = None

    for cellule in recupere_cellules(liste_chainee):
        if fonction(cellule):
            if not cellule_courante_1:
                liste_chainee_1.tete = cellule
            else:
                cellule_courante_1.suivant = cellule
            cellule_courante_1 = cellule
        else:
            if not cellule_courante_2:
                liste_chainee_2.tete = cellule
            else:
                cellule_courante_2.suivant = cellule
            cellule_courante_2 = cellule
