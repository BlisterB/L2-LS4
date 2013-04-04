#!/usr/bin/env python3

'''Cette fonction calcule la somme des entier de 1 à 100 en explicitant le compteur i et en l'incrémentant manuellement, l'utilisation de range(101) permettrait d'économiser des lignes de programmation'''
i = 0
somme = 0
while i <=100 :
    somme += i
    i = i + 1
    print(somme)
