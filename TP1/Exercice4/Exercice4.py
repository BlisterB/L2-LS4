#!/usr/bin/env python3

"""Ma correction de l'exercice 4"""

def somme_bete(x) :
    """Calcule de façon naive la somme des entiers de 1 a x"""
    somme = 0
    for i in range(x+1) :
        somme += i
    print(somme)

def somme_rapide(x) :
    """Calcule de façon rapide la somme des entiers de 1 a x"""
    print(x*(x+1)//2)

def main() :
    """La fonction main"""
    x = 100
    somme = 0
    for i in range(1, x+1) :
        somme+=i
    print(somme)
    if(somme == x*(x+1)/2) :
        print("Le calcul est valide")

    #Q4
    somme_bete(100)
    somme_rapide(100)

if(__name__ == "__main__") :
    main()
