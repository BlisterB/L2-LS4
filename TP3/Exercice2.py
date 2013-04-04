#!/usr/bin/env python3.3

def decoupe(string) :
    return string.split(" ")

def enlevePonctuation(str) :
    import string
    for char in str :
        if char in string.punctuation or string.whitespace :
            str = str.replace(char, " ")
    return str

def listeMotUnique(str) :
    """Retourne une liste contenant les mots apparaissant dans la chaine de caractère, sans doublon"""
    return set(decoupe(str))

def compteNombreMotDifferent(str) :
    """Compte le nombre de mot different dans la chaine de caractere"""
    return len(listeMotUnique(str))

def afficheNombreOccurence(str) :
    """Affiche le nombre d'occurence de chaque mot de la chaine de caractere"""
    for mot in listeMotUnique(str) :
        print("\"{}\" apparait {} fois".format(mot, str.count(mot)))

def textFileToString(filepath) :
    """Prend le chemin d'un fichier texte en parametre et renvoie la chaine de caractère qu'il contient, en remplant la ponctuation et les caractères de saut de ligne/tabulation par des espaces"""
    f = open(filepath, "r")
    return enlevePonctuation(f.read())
    
if __name__ == "__main__" :
    str = textFileToString("phrases.txt")
    print (compteNombreMotDifferent(str))
    afficheNombreOccurence(str)
