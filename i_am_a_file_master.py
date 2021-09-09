#!usr/bin/env Python3
import os
os.chdir("/Users/mathis/Desktop")

fichier = open("toto.py", 'w+')
fichier.write("texte au pif lalala \n")
print("du texte au hasard encore", file = fichier)
fichier.close
