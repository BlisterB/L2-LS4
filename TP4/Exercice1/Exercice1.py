#!/usr/bin/env python3.3

def diviseur(n) :
    return [i for i in range(1, n+1) if n%i == 0]

def premier(n) :
    return [i for i in range(1, n+1) if len(diviseur(i)) <= 2]

def sans_e(liste) :
    return [mot for mot in liste if not mot.__contains__('e')]

def anti_begue(liste) :
    return " ".join([mot for indice, mot in enumerate(liste) if not mot.__eq__(liste[int(indice-1)]) and indice < len(liste)])

def main() :
    #Q1
    liste = [i for i in range(0, 11) if i%2 == 0]
    print(liste)

    #Q2
    liste = [x for x,y in enumerate(range(0, 11)) if y%2==0]
    print(liste)

    #Q3
    print(diviseur(12))

    #Q4
    print(premier(15))

    #Q5
    liste = "Il était une fois".split(" ")
    print(sans_e(liste))

    #Q6
    liste = "Il était était une une fois".split(" ")
    print(anti_begue(liste))
    
if(__name__ == "__main__") :
    main()
