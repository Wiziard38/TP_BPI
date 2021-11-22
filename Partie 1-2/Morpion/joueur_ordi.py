#!/usr/bin/env python3

import morpion
import random

def joue_coup(cases, symbole):
    """
    Fonction qui va faire jouer l'ordinateur pour obtenir un coup au hasard au morpion.
    """
    
    while True:
        num_case = random.randint(0,8)
        if int(cases[num_case]) == num_case:
            return num_case
