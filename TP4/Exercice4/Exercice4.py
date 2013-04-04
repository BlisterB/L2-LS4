#!/usr/bin/env python3.3


def main() :
    #Q2
    chaine = "Ceci est mon message a chiffrer"
    chaine = "".join([chr(ord(lettre) + 3) for lettre in chaine])
    print(chaine)

    #Q3
    chaine = "Ceci est mon message a chiffrer"
    clef = "secret"
    chaine = chaine.split(" ")
    chaineCrypt = ""
    compteur = 0
    for word in chaine :
        for lettre in word :
            chaineCrypt += chr(ord(lettre) + ord(clef[compteur]))
            compteur = compteur + 1
            if compteur == len(clef) - 1 :
                compteur = 0
        chaineCrypt += " "
    print(chaineCrypt)
        

if(__name__ == "__main__") :
    main()
