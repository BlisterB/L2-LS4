#!/usr/bin/env python3.3
import string

def decoupe(chaine) :
    for i in string.whitespace.join(string.punctuation) :
        chaine = chaine.replace(i, "")
    return chaine

def fic_to_dic(chemin) :
    dico = dict()
    fichier = open(chemin, 'r')
    for line in fichier :
        line = line.replace("\n", "")
        line = line.split(":")
        dico[line[0]] = line[1]
    fichier.close()
    return dico

def crypt_by_dic(chemin, dico) :
    fichier = open(chemin)
    nextText = ""
    for line in fichier :
        line = list(line)
        nextText += "".join([dico[lettre] for lettre in line if dico.__contains__(lettre)]) + "\n"
    fichier.close()
    return nextText

def count_occurrences(chemin) :
    fichier = open(chemin)
    dico = {}
    compteurLettreTotal = 0
    for ligne in fichier :
        ligne = ligne.lower();
        ligne = decoupe(ligne)
        compteurLettreTotal += len(ligne)
        for lettre in ligne :
            if string.ascii_letters.__contains__(lettre) :
                if not dico.__contains__(lettre) :
                    dico[lettre] = 1
                else :
                    dico[lettre] = int(dico[lettre]) + 1
    #On calcule les ratio
    for indice in dico :
        dico[indice] = dico[indice]*100/compteurLettreTotal
    return dico   
        

def main() :
    chemin = "dico.txt"
    dico = fic_to_dic(chemin)
    crypt_by_dic("educ.txt", dico)
    count_occurrences("educ.txt")

if(__name__ == "__main__") :
    main()
