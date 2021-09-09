#!usr/bin/env python3

"""Module d'encodage/décodage par rotation"""
import string

def rot(decalage, lettre):
    """Renvoie la lettre donnée encodée par rotation.

    Le décalage utilisé pour la rotation est spécifié en paramètre.
    Préconditions :
       - lettre est une chaîne de caractère de taille 1 ;
       - lettre est un soit une lettre majuscule
         soit une lettre minuscule.
    """
    
    # Verification des conditions
    if (lettre not in string.ascii_letters) or (len(lettre) != 1): # On verifie les conditions
        return 
    
    if lettre in string.ascii_lowercase: # si c'est une minuscule
        return chr((ord(lettre) + decalage - 97)%26 +97)
    else: # Sinon c'est une majuscule
        return chr((ord(lettre) + decalage - 65)%26 +65)

def rot13(lettre):
    """Encode la lettre donnée par rotation de 13 caractères 
    (correspond au nombre de lettre du nom du TP !).

    Pour répondre à une question qui revient souvent :
    "Oui cette fonction est ultra simple, et s'implémente
    en une seule ligne".

    Préconditions :
       - lettre est une chaîne de caractères de taille 1.
    """
    
    if (lettre not in string.ascii_letters) or (len(lettre) != 1): # On verifie les conditions
        return 
    
    if lettre in string.ascii_lowercase: # si c'est une minuscule
        return chr((ord(lettre) + 13 - 97)%26 +97)
    else: # Sinon c'est une majuscule
        return chr((ord(lettre) + 13 - 65)%26 +65)