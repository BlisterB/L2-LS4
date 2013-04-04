#!/usr/bin/env python3

'''Cette fonciont calcule la somme des entier de 1 à 100 en utilisant la méthode range qui génère tous les entier de 1 à 100, ça permet d'économiser des ligne de programmation'''
somme = 0
for i in range(101) :
    somme += i
    print(somme)
