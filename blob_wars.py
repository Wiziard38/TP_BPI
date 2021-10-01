#!/usr/bin/env python3

from copy import deepcopy

def init():
    """
    """
    tableau = [False]*64
    tableau[63] = 'bleu'
    tableau[56] = 'bleu'
    tableau[7] = 'rouge'
    tableau[0] = 'rouge'
    return tableau


def affiche_tab(tableau):
    """
    Fonction qui va afficher le plateau de jeu sur le terminal.
    """
    form = "{0:^3}{1:^3}{2:^3}{3:^3}{4:^3}{5:^3}{6:^3}{7:^3}"
    tab = [[0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8, [0]*8]

    for i in range(8):
        for j in range(8):
            print(i,j)
            if tableau[i + j*8] == 'rouge':
                tab[i][j] = '\u001b[31m \u25CF \u001b[0m'
            elif tableau[i + j*8] == 'bleu':
                tab[i][j] = '\u001b[34m \u25CF \u001b[0m'
            else:
                if 0 < 63 - (i*8 + j) < 10:
                    tab[i][7-j] = '0' + str(63 - (i*8 + j))
                else:
                    tab[i][7-j] = 63 - (i*8 + j)

    print()
    for val in tab:
        print(form.format(*val))
    print()


def jeu_blob(tableau):
    """
    """
    joueur = 'bleu'
    while True:
        print(f"Joueur {joueur} veuillez entrer un coup")
        print("Le format doit etre 'depart arrivee', par exemple '0 8'")
        (depart, arrivee) = input("C'est a vous : ").split(' ')
        if not(coup_valide(int(depart), int(arrivee), joueur, tableau)):
            print('coup invalide')
        else:
            type_coup = type_coup(depart, arrivee)
            if type_coup == 'normal':
                tableau[arrivee] = joueur

                # prochain joueur
                liste_joueurs = ['rouge', 'bleu']
                liste_joueurs.remove(joueur)
                joueur = liste_joueurs[0]

            else:
                tableau[depart] = False
                tableau[arrivee] = joueur
                

def changement_saut(arrivee, joueur, tableau):
    """
    Fonction qui va changer les couleurs selon les regles du saut.
    """
    ...

def type_coupe(depart, arrivee):
    """
    Fonction qui renvoie le type de coup joue, soit un saut soit
    un deplacement simple.
    """
    ligne_dep = depart // 8
    colonne_dep = depart % 8
    ligne_arr = arrivee // 8
    colonne_arr = arrivee % 8
    if max(max(ligne_dep, ligne_arr) - min(ligne_dep, ligne_arr), 
                    max(colonne_dep, colonne_arr) - min(colonne_dep, colonne_arr)) == 1:
        return 'normal'
    return 'saut'


def coup_valide(depart, arrivee, joueur, tableau):
    """
    Verifie la validite d'un coup joué.
    """
    if tableau[depart] == joueur:
        if not(tableau[arrivee]):
            ligne_dep = depart // 8
            colonne_dep = depart % 8
            ligne_arr = arrivee // 8
            colonne_arr = arrivee % 8
            if max(max(ligne_dep, ligne_arr) - min(ligne_dep, ligne_arr), 
                    max(colonne_dep, colonne_arr) - min(colonne_dep, colonne_arr)) < 2:
                return True
    return False


def main():
    tab = init()
    affiche_tab(tab)

if __name__ == '__main__':
    main()