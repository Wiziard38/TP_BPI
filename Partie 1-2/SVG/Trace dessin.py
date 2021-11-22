#!/usr/bin/env python3

"""Programme pour tester le module logo."""

import os
os.chdir("/Users/mathis/Desktop/TP_BPI/SVG")
import logo
import svg

def main():
    """On crée un dessin a l'aide du module logo."""
    image = open('Mon dessin.svg', 'w+')

    # Dimensions de l'image
    hauteur = int(input("Quelle hauteur de l'image ? \n > "))
    largeur = int(input("Quelle largeur de l'image ? \n > "))
    image.write(svg.genere_balise_debut_image(largeur, hauteur))

    # En python on peut nommer les arguments quand on appelle une
    # fonction. Cela rend le code beaucoup plus lisible en général.

    couleur = input("Quelle couleur de ligne voulez-vous choisir (en anglais) ? \n > ")
    epaisseur = input("Quelle epaisseur de ligne voulez-vous choisir ? \n > ")
    image.write(svg.genere_balise_debut_groupe(couleur_ligne = couleur,
                                         couleur_remplissage="none",
                                         epaisseur_ligne = epaisseur))

    # Notre tortue est représentée par 4 infos :
    abscisse = float(input(f"A quelle abscisse voulez vous commencer votre dessin (entre 0 et {largeur}) ? \n > "))
    ordonnee = float(input(f"A quelle ordonnee voulez vous commencer votre dessin (entre 0 et {hauteur}) ? \n > "))
    direction = float(input(f"Selon quel angle voulez vous debuter (entre 0 et 360˚) ? \n > "))  # angle du regard de la tortue en degrés
    
    crayon_en_bas = True
    while True:
        choix = input(f"Que voulez vous faire ? \n Position actuelle : abs = {abscisse}, ord = {ordonnee}, angle = {direction} \
                                                \n - Avancer (a) \
                                                \n - Tourner a droite (d) \
                                                \n - Tourner a gauche (g) \
                                                \n - Arreter (x) \
                                                \n - Changer la position du crayon, actuellement il est " + ("posé" if crayon_en_bas else "levé") + " (c) \
                                                \n > ")
        if choix == 'x':
            break
        elif choix == 'a':
            distance =  int(input("De combien voulez vous avancer ? \n > "))
            abscisse, ordonnee, sortie = logo.avance(abscisse, ordonnee, direction, crayon_en_bas, distance)
            image.write(sortie)
        elif choix == 'd':
            rotation = int(input("De combien voulez vous tourner a droite ? \n > "))
            direction = logo.tourne_droite(direction, rotation)
        elif choix == 'g':
            rotation = int(input("De combien voulez vous tourner a gauche ? \n > "))
            direction = logo.tourne_gauche(direction, rotation)
        elif choix == 'c':
            crayon_en_bas = crayon_en_bas ^ True

    image.write(svg.genere_balise_fin_groupe())
    image.write(svg.genere_balise_fin_image())
    image.close()

if __name__ == "__main__":
    main()