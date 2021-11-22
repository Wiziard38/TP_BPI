#!usr/bin/env python3
""" Fichier comprenant des listes chainees. """

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

class ListeSimplementChainee:
    """ Une liste simplement chaînée.
    Possède une référence vers la tête de liste.
    """
    def __init__(self):
        self.tete = None

def ajoute_en_tete(liste_chainee, valeur):
    """ Ajoute une cellule en tete. """
    nouvelle_tete = Cellule(valeur, liste_chainee.tete)
    liste_chainee.tete = nouvelle_tete

def ajoute_en_queue(liste_chainee, valeur):
    """ Ajoute une cellule en queue. """
    cellule_queue = Cellule(valeur, None)
    liste_chainee.queue.suivant = cellule_queue

def recupere_cellules(liste_chainee):
    """ Renvoie un vecteur contenant toutes les cellules de la liste_chainee. """
    liste_valeur = []
    cellule = liste_chainee.tete
    while cellule.suivant.valeur is not None:
        liste_valeur.append(cellule.valeur)
        cellule = cellule.suivant
    return liste_valeur

def recherche(liste_chainee, valeur):
    """Recherche uen valeur dans la liste_chainee donnée.
    Renvoie la premiere cellule contenant la valeur donnée ou
    None si la valeur n'est pas trouvée dans la liste_chainee.
    """
    cellule = liste_chainee.tete
    while cellule.suivant is not None:
        if cellule.valeur == valeur:
            return cellule
        cellule = cellule.suivant

def supprime(liste_chainee, valeur):
    """Enleve la premiere cellule contenant la valeur donnée."""
    cellule = liste_chainee.tete
    if cellule.valeur == valeur:
        liste_chainee.tete = cellule.suivant

    cellule_memoire = liste_chainee
    while cellule.suivant is not None:
        if cellule.valeur == valeur:
            cellule_memoire.suivant = cellule.suivant
        cellule_memoire = cellule
        cellule = cellule.suivant

def test_listes():
    """On teste les operations de base, dans differentes configurations."""
    liste_chainee = ListeSimplementChainee()
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_0")
    ajoute_en_tete(liste_chainee, 3)
    ajoute_en_tete(liste_chainee, 5)
    ajoute_en_tete(liste_chainee, 2)
    ajoute_en_tete(liste_chainee, 4)
    print("liste_chainee : ", liste_chainee)
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_1")
    print("recherche : ", recherche(liste_chainee, 3).valeur)
    supprime(liste_chainee, 5)
    print("apres suppression de 5 : ", liste_chainee)
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_2")
    supprime(liste_chainee, 4)
    print("apres suppression de 4 : ", liste_chainee)
    traceur.display_instance(liste_chainee,
                             visualize=False,
                             image_name="liste_chainee_3")

if __name__ == "__main__":
    test_listes()
