#!/bin/usr/env Python3.3

def decoupe(chaine) :
    import string
    for i in string.punctuation :
        chaine = chaine.replace(i, "")
    chaine = chaine.split(" ")
    return chaine

def compteMot(chaine) :
    chaine = decoupe(chaine.lower())
    liste = list()
    for i in chaine :
        if not liste.__contains__(i) :
            liste.append(i)
    return len(liste)

def occurenceMot(chaine) :
    chaine = decoupe(chaine.lower())
    motDejaCite = list()
    for i in chaine :
        if not motDejaCite.__contains__(i) :
            print("\"{}\" apparait {} fois dans la chaine : \"{}\"".format(i, chaine.count(i), " ".join(chaine)))
            motDejaCite.append(i)

def lisFichier(chemin) :
    fichier = open(chemin, "r")
    for i in fichier :
        occurenceMot(i)

def main() :
    chaine = "Il il etait etAIt une une fois fois"
    print("Il y a {} mots differents dans {}".format(compteMot(chaine), chaine))
    occurenceMot(chaine)

    #Q4
    chemin = "phrase.txt"
    print("\nLisons le fichier {} :".format(chemin))
    lisFichier(chemin)

if(__name__ == "__main__") :
    main()
