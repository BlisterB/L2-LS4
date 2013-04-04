#!/usr/bin/env python3
import sys, random

dico= dict()

def fileToDict(path) :
    try :
        f = open(path, "r")
        for string in f :
            tab = string.split(",")
            assert len(tab) == 2
            dico[tab[0]] = tab[1]
        f.close
        return dico
    except IOError :
        print("Le fichier n'existe pas")
    except AssertionError :
        print("Toutes les lignes du tableau doivent être de la forme \"pays, capitale\"")

def quizzCity(city) :
    if city+"\n" in dico.values() :
        answer = input("Quelle est le pays dont " + city + " est la capitale ?")
        if answer in dico.keys() :
            if dico[answer] == city+"\n" : 
                print("Exact !")
            else :
                print("Faux...")
        else :
            print("Ce pays n'est pas repertoriée !")
    else :
        print("Cette ville n'est pas repertoriée !")

def quizzRandom() :
    country = random.choice(list(dico))
    answer = input("Quelle est la capital de ce pays : {} ?\n".format(country))
    if(answer == dico[country]) :
        print(Exact) !

if __name__ == "__main__" :
    dico = fileToDict("capitales.txt")
    commande = sys.argv
    if len(commande)>1 :
        if commande[1] == "-v" :
            if len(commande) == 3 :
                quizzCity(commande[2])
        elif commande[1] == "-n" :
            quizzRandom()
    else :
        print("La fonction doit etre appelée avec l'option -v ville ou l'option -n")
