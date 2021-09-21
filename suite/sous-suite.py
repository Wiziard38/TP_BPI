#!/usr/bin/env python3

import os
import sys
os.chdir("/Users/mathis/Desktop/TP_BPI/suite")


def genere_suites(chemin_fichier):
    """
    Permet de lire tout un fichier de nombre donne en parametre.
    """
    suites = []
    sous_suite = []
    type_suite = ''

    fichier = open(chemin_fichier, 'r')

    for ligne in fichier:
        for nombre in ligne[0:-1].split(' '):
            if len(sous_suite) == 0:
                sous_suite.append(int(nombre))
            elif not type_suite:
                sous_suite.append(int(nombre))
                if sous_suite[-1] != sous_suite[-2]:
                    type_suite = ('croissante' if (sous_suite[-1] > sous_suite[-2]) else 'decroissante')
            else:
                (etat, type_suite) = traite_nombre(sous_suite, type_suite, int(nombre))
                if etat:
                    sous_suite.append(int(nombre))
                else:
                    suites.append(sous_suite.copy())
                    debut = sous_suite[-1]
                    for i in range(len(sous_suite)):
                        if sous_suite[i] == debut:
                            sous_suite = sous_suite[i:]
                            sous_suite.append(int(nombre))
                            break
    
    fichier.close()
    return suites
            

def traite_nombre(suite, type_suite, nombre):
    """ 
    Traite le nombre donné vis à vis de la suite donnée.

    Renvoie (True, nouveau_type_suite) si suite est toujours
    une suite monotone après ajout de nombre.
    Renvoie (False, nouveau_type_suite) si la suite à changer de sens
    """
    
    if type_suite == "croissante":
        if suite[-1] <= nombre:
            return (True, 'croissante')
        else:
            return (False, 'decroissante')
    else: # type decroissante
        if suite[-1] >= nombre:
            return (True, 'decroissante')
        else:
            return (False, 'croissante')


def main():
    if len(sys.argv) != 2 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("utilisation:", sys.argv[0], "chemin_fichier")
        sys.exit(1)
    
    print(max(genere_suites(sys.argv[1]), key = len))

if __name__ == '__main__':
    main()