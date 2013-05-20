#!/usr/bin/env python3

def inversion() :
    phrase = input("Veuillez entrer une phrase :")
    liste = phrase.split(" ")
    liste.reverse()
    return liste

def inverse(mot) :
    l = list(mot)
    l.reverse()
    return "".join(l)

def palyndrome(phrase) :
    import string
    for c in phrase :
        if c in  string.punctuation :
            phrase = phrase.replace(c, "")
    tableauDeMot = phrase.split(" ")
    l = list()
    for mot in tableauDeMot :
        if (mot == inverse(mot)) :
            l.append(mot)
    return l

def inclu(liste1, liste2) :
    return str(liste1)[1:-1] in str(liste2)[1:-1]
            

if __name__ == "__main__" :
    print(palyndrome("ae;a azer azereza"))
    print(str([1, 2, 3, 4])[1:-1])
