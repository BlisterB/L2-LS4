#!/usr/bin/python3.2

annee = input("Bonjour, quelle annee voulez vous tester ?\n")

estBisextile = False

if annee % 4 == 0 :
    if annee % 100 == 0 :
        if annee % 400 == 0 :
            estBisextile = True
    else :
        estBisextile = True

#Affichage du resultat
if estBisextile :
    print("L'annee est bisextile !")
else :
    print("L'annee n'est pas bisextile..")
    
