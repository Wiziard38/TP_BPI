#!/usr/bin/env python3

def pivote(tableau, pivot):
    """
    Fonction qui permet la separation en deux tableau selon les elements plus grands
    ou plus petits que le pivot.
    """

    valeur = tableau[pivot]
    tableau.pop(pivot)
    tab_inf = [i for i in tableau if i <= valeur]
    tab_sup = [i for i in tableau if i > valeur]

    return tab_inf, tab_sup

def pivote_enplace(tableau, pivot):
    """
    Fonctions qui permet la separation en place d'un tableau selon un pivot.
    """

    valeur = tableau[pivot]
    nb_val_inf = 0

    if pivot != 0:
        tableau[pivot] = tableau[0]
        tableau[0] = valeur

    for i in range(1, len(tableau)):
        if tableau[i] <= valeur:
            tmp = tableau[i]
            tableau[i] = tableau[nb_val_inf + 1]
            tableau[nb_val_inf + 1] = valeur
            tableau[nb_val_inf] = tmp
            nb_val_inf += 1
    
    return tableau
        

def main():
    tab = [3, 0, 10, 1, 6, 9, 5, 3, 9, 0, 5, 8, 9, 8, 4, 2, 0, 9, 6, 2]
    print(pivote_enplace(tab, 0))

if __name__ == '__main__':
    main()