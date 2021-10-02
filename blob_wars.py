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
            if tableau[63 - (i*8 + j)] == 'rouge':
                tab[i][7-j] = '\u001b[31m \u25CF \u001b[0m'
            elif tableau[63 - (i*8 + j)] == 'bleu':
                tab[i][7-j] = '\u001b[34m \u25CF \u001b[0m'
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
    Fonction qui va faire jouer les deux humains.
    """
    joueur = 'bleu'
    while True:

        if fin_partie(tableau, joueur):
            affiche_tab(tableau)
            gagnant(tableau)
            break
        
        affiche_tab(tableau)

        print(f"Joueur {joueur} veuillez entrer un coup")
        print("Le format doit etre 'depart arrivee', par exemple '0 8'")
        (depart, arrivee) = input("C'est a vous : ").split(' ')
        (depart, arrivee) = (int(depart), int(arrivee))
        if not(coup_valide(depart, arrivee, joueur, tableau)):
            print('coup invalide')
        else:
            coup = type_coup(depart, arrivee)
            if coup == 'normal':
                tableau[arrivee] = joueur
            else:
                tableau[depart] = False
                tableau[arrivee] = joueur
                changement_saut(arrivee, joueur, tableau)
            
            # prochain joueur
            liste_joueurs = ['rouge', 'bleu']
            liste_joueurs.remove(joueur)
            joueur = liste_joueurs[0]


def gagnant(tableau):
    """ Fonction qui retourne quel est le gagnant d'une
    partie qui est finie. """
    cases_bleues = tableau.count('bleu')
    cases_rouges = tableau.count('rouge')
    if cases_rouges > cases_bleues:
        print('Le gagnant est le joueur rouge !')
    elif cases_bleues > cases_rouges:
        print('Le gagnant est le joueur bleu !')
    else:
        print('Égalité !')


def changement_saut(arrivee, joueur, tableau):
    """
    Fonction qui va changer les couleurs selon les regles du saut.
    """
    liste_joueurs = ['bleu', 'rouge']
    liste_joueurs.remove(joueur)
    joueur2 = liste_joueurs[0]
    (ligne_arr, colonne_arr) = get_lignecolonne(arrivee)

    def changement(ligne, colonne, tableau, joueur, joueur2):
        """ Inversion de couleur dans le tableau """
        if tableau[ligne*8 + colonne] == joueur2:
            tableau[ligne*8 + colonne] = joueur
        return tableau

    if ligne_arr != 7:
        changement(ligne_arr + 1, colonne_arr, tableau, joueur, joueur2)
        if colonne_arr != 7:
            changement(ligne_arr, colonne_arr + 1, tableau, joueur, joueur2)
            changement(ligne_arr + 1, colonne_arr + 1, tableau, joueur, joueur2)
        if colonne_arr != 0:
            changement(ligne_arr, colonne_arr - 1, tableau, joueur, joueur2)
            changement(ligne_arr + 1, colonne_arr - 1, tableau, joueur, joueur2)
    if ligne_arr != 0:
        changement(ligne_arr - 1, colonne_arr, tableau, joueur, joueur2)
        if colonne_arr != 7:
            changement(ligne_arr - 1, colonne_arr + 1, tableau, joueur, joueur2)
        if colonne_arr != 0:
            changement(ligne_arr - 1, colonne_arr - 1, tableau, joueur, joueur2)

    return tableau


def fin_partie(tableau, joueur):
    """
    Fonction qui va renvoyer vrai ou faux en fonction de 
    si une partie est terminee ou non.
    """
    
    def check_cases(tableau, case):
        """ Fonction pour verifier si il y a une case ou le mouvement
        est possible dans les alentours d' une case donnee. """
        
        def get_24cases(tableau, case):
            """ Renvoie une list contenant les 24 cases entourant 1 case. """
            (ligne, colonne) = get_lignecolonne(case)
            liste_cases = []

            if ligne != 0:
                liste_cases.append(tableau[(ligne - 1)*8 + colonne]) # 6
                if colonne != 0:
                    liste_cases.append(tableau[ligne*8 + colonne - 1]) # 8
                    liste_cases.append(tableau[(ligne - 1)*8 + colonne - 1]) # 7
                    if colonne != 1:
                        liste_cases.append(tableau[ligne*8 + colonne - 2]) # 23
                        liste_cases.append(tableau[(ligne - 1)*8 + colonne - 2]) # 22
                if colonne != 7:
                    liste_cases.append(tableau[ligne*8 + colonne + 1]) # 4
                    liste_cases.append(tableau[(ligne - 1)*8 + colonne + 1]) # 5
                    if colonne != 6:
                        liste_cases.append(tableau[ligne*8 + colonne + 2]) # 15
                        liste_cases.append(tableau[(ligne - 1)*8 + colonne + 2]) # 16
                if ligne != 1:
                    liste_cases.append(tableau[(ligne - 2)*8 + colonne]) # 19
                    if colonne != 0:
                        liste_cases.append(tableau[(ligne - 2)*8 + colonne - 1]) # 20
                        if colonne != 1:
                            liste_cases.append(tableau[(ligne - 2)*8 + colonne - 2]) # 21
                    if colonne != 7:
                        liste_cases.append(tableau[(ligne - 2)*8 + colonne + 1]) # 18
                        if colonne != 6: 
                            liste_cases.append(tableau[(ligne - 2)*8 + colonne + 2]) # 17
            if ligne != 7:
                liste_cases.append(tableau[(ligne + 1)*8 + colonne]) # 2
                if colonne != 0:
                    liste_cases.append(tableau[(ligne + 1)*8 + colonne - 1]) # 1
                    if colonne != 1:
                        liste_cases.append(tableau[(ligne + 1)*8 + colonne - 2]) # 24
                if colonne != 7:
                    liste_cases.append(tableau[(ligne + 1)*8 + colonne + 1]) # 3
                    if colonne != 6:
                        liste_cases.append(tableau[(ligne + 1)*8 + colonne + 2]) # 14
                if ligne != 6:
                    liste_cases.append(tableau[(ligne + 2)*8 + colonne]) # 11
                    if colonne != 0:
                        liste_cases.append(tableau[(ligne + 2)*8 + colonne - 1]) # 10
                        if colonne != 1:
                            liste_cases.append(tableau[(ligne + 2)*8 + colonne - 2]) # 9
                    if colonne != 7:
                        liste_cases.append(tableau[(ligne + 2)*8 + colonne + 1]) # 12
                        if colonne != 6:
                            liste_cases.append(tableau[(ligne + 2)*8 + colonne + 2]) # 13
            return liste_cases

        ###
        cases = get_24cases(tableau, case)
        if False in cases:
            return True
        return False
            
    ###
    if joueur not in tableau:
        return True
    for case, contenu in enumerate(tableau):
        if contenu == joueur:
            if not(check_cases(tableau, case)):
                return True
    return False


def get_lignecolonne(position):
    """
    Fonction qui recupere le numero de ligne et de colonne de 
    la case de depart et celle d'arrivee.
    """
    ligne = position // 8
    colonne = position % 8
    return(ligne, colonne)


def type_coup(depart, arrivee):
    """
    Fonction qui renvoie le type de coup joue, soit un saut soit
    un deplacement simple.
    """
    (ligne_dep, colonne_dep) = get_lignecolonne(depart)
    (ligne_arr, colonne_arr) = get_lignecolonne(arrivee)
    if max(max(ligne_dep, ligne_arr) - min(ligne_dep, ligne_arr), 
                    max(colonne_dep, colonne_arr) - min(colonne_dep, colonne_arr)) == 1:
        return 'normal'
    return 'saut'


def coup_valide(depart, arrivee, joueur, tableau):
    """
    Verifie la validite d'un coup joué.
    """

    if 0 <= depart <= 63 and 0 <= arrivee <= 63:
        if tableau[depart] == joueur:
            if not(tableau[arrivee]):
                (ligne_dep, colonne_dep) = get_lignecolonne(depart)
                (ligne_arr, colonne_arr) = get_lignecolonne(arrivee)
                if max(max(ligne_dep, ligne_arr) - min(ligne_dep, ligne_arr), 
                        max(colonne_dep, colonne_arr) - min(colonne_dep, colonne_arr)) <= 2:
                    return True
    return False


def main():
    tab = init()
    jeu_blob(tab)

if __name__ == '__main__':
    main()