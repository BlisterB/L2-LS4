#!/usr/bin/env python3

def read_lexic(nomFichier) :
    dictionnaire = dict()
    fichier = open(nomFichier, "r")
    for ligne in fichier :
        if ligne != "" :
            tableau = ligne.split(":")
            if len(tableau) == 2 :
                dictionnaire[tableau[0]] = tableau[1]
    fichier.close()
    return dictionnaire

def write_lexic(nomFichier, dictionnaire) :
    fichier = open(nomFichier, "w")
    for i in sorted(dictionnaire) :
        fichier.write("{0}:{1}".format(i, dictionnaire[i]))
    fichier.close()

def translate_word(dictonnaire, mot) :
    try :
        return dictonnaire[mot]
    except KeyError :
        return "Aucun mot correspondant dans le dictionnaire" 

def add_word(dictionnaire, mot, traduction) :
    dictionnaire[mot] = traduction+"\n"

def print_dict(dictionnaire) :
    for i in sorted(dictionnaire) :
        print(i + " -> " + dictionnaire[i])

def main() :
    dictionnaire = read_lexic("dico.txt")
    mot = input("Quel mot voulez-vous traduite ?\n")
    traduction = translate_word(dictionnaire, mot)
    if traduction != "Aucun mot correspondant dans le dictionnaire" :
        print("La traduction de {0} est {1}\n".format(mot, traduction))
    elif mot.find(" ") != -1 :
        print("Le mot doit être de longueur 1")
    else :
        reponse = input("Ce mot n'existe pas, voulez-vous l'ajouter au dictionnaire ?(oui/non)\n")
        if reponse == "oui" :
            traduction = input("Quel est sa traduction ?")
            if traduction.find(" ") == -1 :
                add_word(dictionnaire, mot, traduction)
            else :
                print("Le mot doit être de longueur 1")
    choixSauvegarder = input("Voulez vous sauvegarder le dictionnaire ? (oui/non)")
    if choixSauvegarder == "oui" :
        write_lexic("dico.txt", dictionnaire)
    

if __name__ == "__main__" :
    main()
