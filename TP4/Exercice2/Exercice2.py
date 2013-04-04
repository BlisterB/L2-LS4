#!/usr/bin/env python3.3
import grandes_lettres

def grand_message(str) :
    ligne = ""
    str = str.lower()
    for i in range(0, 5) :
        for lettre in str :
            ligne += grandes_lettres.ligne(i, lettre)
            ligne += " "
        ligne += "\n"
    print(ligne)            

if(__name__) == "__main__" :
    grand_message(input("Veuillez entrer une chaine de caractere :"))
