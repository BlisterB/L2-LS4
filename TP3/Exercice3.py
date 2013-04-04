#!/usr/bin/env python3.3

def read_lexic(pathName) :
    """Prend en paramètre le chemin d'un fichier texte et renvoit le dictionnaire associé
    On considere qu'une ligne est construite de cette manière :
    mot:traduction1,traduction2,...,traductionN"""
    import string
    #Ouverture du fichier
    try :
        file = open(pathName, "r")
    except IOError :
        print("Fichier non existant ou invalide")

    #Creation du dictionnaire :
    dico = dict()  
    for line in file :
        print(line)###
        str = line
        #On enveve les tabulations :
        for char in string.whitespace :
           str = str.replace(char, "")
        #Creation de la liste contenant les traduction du mot
        wordList = str.split(":")
        tradList = wordList[1].split(",")
        dico[wordList[0]] = tradList
        print(dico)

    file.close()
    return dico

def write_lexic(pathName, dico) :
    try :
        file = open(pathName, "w")
    except IOError :
        print("Fichier non existant ou invalide")

    #Construction du fichier :
    for word in dico :
        #Creation de la ligne
        trad = ""
        if word != "" :
            for cle in dico[word] :
                if trad == "" :
                    trad = "{}".format(cle)
                else :
                    trad = "{},{}".format(trad, cle)
            #Ajout de la ligne dans le fichier
        file.write("{}:{}\n".format(word, trad))
    file.close()

def translate_word(dico, word) :
    return dico[word]

def add_word(dico, word, translation) :
    """Retourne le dico dans lequel on a ajouté word (si doc ne le contenait pas) ainsi que sa traduction translation"""
    #On regarde si translation est list ou str, puis on crée un liste
    if type(translation) == str :
        l = list()
        l.append(translation)
    if type(translation) == list :
        l = translation
    #On ajoute la liste des traduction
    if dico.__contains__(word):
        for transl in l :
            if not dico[word].__contains__(transl) :
                dico[word].append(transl)
    else :
        dico[word] = l
    return dico

def main() :
    dic = read_lexic("dico.txt")
    print(dic)
    dic = add_word(dic, "mot2", ["trad10", "trad11", "trad12"])
    print(dic)
    write_lexic("dico.txt", dic)

if __name__ == "__main__" :
    main()
