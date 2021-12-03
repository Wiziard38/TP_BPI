#!/usr/bin/env python3

import sys
from collections import deque
import matplotlib.pyplot as plt
import time

class CelluleSimple:
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant

class CelluleDouble:
    def __init__(self, valeur, suivant, precedent):
        self.valeur = valeur
        self.suivant = suivant
        self.precedent = precedent

class ListeSimplementChainee:
    def __init__(self, mot):
        premiere_cellule = None
        for lettre in reversed(mot):
            premiere_cellule = CelluleSimple(lettre, premiere_cellule)
        self.tete = premiere_cellule

class ListeDoublementChainee:
    def __init__(self, mot):
        iter_lettres = iter(reversed(mot))

        premiere_cellule = CelluleDouble(next(iter_lettres), None, None)
        self.queue = premiere_cellule

        cellule_precedente = premiere_cellule
        for lettre in iter_lettres:
            premiere_cellule = CelluleDouble(lettre, premiere_cellule, None)
            cellule_precedente.precedent = premiere_cellule
        self.tete = premiere_cellule

def remove_simple(liste_simple_chainee):
    cellule_courante = liste_simple_chainee.tete
    if cellule_courante is not None:
        if cellule_courante.suivant is not None:
            while cellule_courante.suivant.suivant is not None:
                cellule_courante = cellule_courante.suivant
            cellule_courante.suivant = None
        else:
            liste_simple_chainee.tete = None

def remove_double(liste_double_chainee):
    derniere_cellule = liste_double_chainee.queue
    if derniere_cellule is not None:
        if derniere_cellule.precedent is not None:
            liste_double_chainee.queue = derniere_cellule.precedent
            derniere_cellule.precedent.suivant = None
        else:
            liste_double_chainee.queue = None
            liste_double_chainee.tete = None

def main():
    number = int(sys.argv[1])

    list_times_simple = []
    list_times_double = []
    list_times_module = []
    liste_simple_chainee = ListeSimplementChainee('a'*number)
    liste_double_chainee = ListeDoublementChainee('a'*number)
    liste_module_chainee = deque(iter('a'*number))

    for _ in range(number//10):
        # liste simple :
        temps = 0
        for _ in range(10):
            tmp = time.time()
            remove_simple(liste_simple_chainee)
            temps += time.time() - tmp
        list_times_simple.append(temps)

        # liste double :
        temps = 0
        for _ in range(10):
            tmp = time.time()
            remove_double(liste_double_chainee)
            temps += time.time() - tmp
        list_times_double.append(temps)

        # liste module :
        temps = 0
        for _ in range(10):
            tmp = time.time()
            liste_module_chainee.pop()
            temps += time.time() - tmp
        list_times_module.append(temps)

    list_number = list(range(number, 0, -10))
    plt.plot(list_number, list_times_simple, label='liste simple')
    plt.plot(list_number, list_times_double, label='liste double')
    plt.plot(list_number, list_times_module, label='deque')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
