#!/usr/bin/env python3.3


def main() :
    #Liste des entiers pairs entre 0 et 10
    l1 = [i for i in range(1, 10) if i%2==0]
    print(l1)

    #Sous-liste des éléments de rang pair d'une liste donnée
    l2 = [y for x, y in enumerate(l1) if x % 2 ==0]
    print(l2)

if __name__ == "__main__" :
    main()
