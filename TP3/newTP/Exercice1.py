#!/usr/bin/env python3.3

def inverse(mot) :
    mot = mot[::-1]
    return "".join(mot)

def decoupe(chaine) :
    import string
    for i in string.punctuation.join(string.whitespace) :
        chaine.replace(i, "")
    return chaine.split(" ");

def palindrome(chaine) :
    liste = decoupe(chaine)
    """Affiche les palindrome de la liste en parametre"""
    boolean = False
    for mot in liste :
        if mot == inverse(mot).lower():
            print("{} est un palindrome".format(mot))
            boolean = True
    if boolean == False :
        print("Aucun mot de la chaine n'est pas un palindrome")

def inclus(liste1, liste2) :
    """Affiche si les éléments de la liste 1 sont inclus dans la liste 2"""
    i = 0
    for i in range(0, len(liste1)) :
        if not liste2[i:].__contains__(liste1[i]) :
            print("Les éléments de liste 1 ne sont pas inclus dans liste 2")
            return
    print("Les éléments de liste 1 sont inclus dans liste 2")

        
def main() :
    l = [i for i in range(0, 11)]

    mot="Gauthier"
    #Q3
    print(inverse(mot))

    #Q4
    chaine = "Il était une fois aaa"
    palindrome(chaine)

    #Q5
    liste1 = [i for i in range(0, 11) if i%2==0]
    liste2 = [i for i in range(0, 11)]
    print("Liste 1 : {}\nListe 2 : {}".format(liste1, liste2))
    inclus(liste2, liste1)
    
if(__name__ == "__main__") :
    main()
