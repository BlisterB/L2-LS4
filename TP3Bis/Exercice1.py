#!/usr/bin/env python3.3

import math

def est_premier(a) :
    """Teste si a est un premier en regardant s'il possède
    un diviseur parmi les entiers inférieurs à sa racine carrée"""
    a = int(a)
    #Test des valeurs dont le systeme de racine carree pose probleme
    if (a == 1) or (a == 2) or (a == 3) :
        return True
    #Test pour les autres valeurs
    racA=(int(a**(1/2)))
    for i in range(2, racA + 1) :
        if a % i == 0 :
            return False
    #Le test est termine
    return True

def liste_premiers_inferieur(a) :
    """Retourne la liste des nombres premiers inférieurs à a"""
    l = list()
    for i in range(1, a + 1) :
        if est_premier(i) :
            l.append(i)
    return l

def liste_premiers_inferieur_eratosthene(a) :
    #Generation de la liste originale
    l = [x in x for range(2, a+1)]


def main() :
    #print(est_premier(input("Est un nombre entier : ")))
    print(liste_premiers_inferieur(10))

if __name__ == "__main__" :
    main()
