#!usr/env/bin Python3

import rotx

def main():
    """ Fonction globale permettant diverses actions """

    # Nom du TP decode
    nom_fichier = input("Saisissez le nom de votre fichier : \n > ") + '.txt'
    fichier = open(nom_fichier, 'w+')
    for letter in 'nirPrfne':
        fichier.write(rotx.rot(26-13, letter))
    
    # Prenom encode
    print(rotx.rot(4, 'M'), rotx.rot(4, 'a'), rotx.rot(4, 't'), rotx.rot(4, 'h'), rotx.rot(4, 'i'), rotx.rot(4, 's'), sep = '')

main()