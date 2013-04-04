#!/usr/bin/env python3.3

def prefixe(mot) :
    return [mot[:i] for i in range(0, len(mot)+1)]

def est_sans_prefixe_cube(mot) :
    return not mot.startswith(3*mot[0])

def est_sans_suffixe_cube(mot) :
    return not mot.endswith(3*mot[0])

def est_sans_cube(mot) :
    for mot in prefixe(mot)[2:] :
        if not est_sans_suffixe_cube(mot) :
            return True
    return False

def main() :
    #Q2
    mot = "Ungrandmot"
    print(prefixe(mot))

    #Q3
    mot = "aabab"
    print("{} possede-t-il un cube comme prefixe ? {}".format(mot, est_sans_prefixe_cube(mot)))

    #Q4
    mot = "abaabab"
    print("{} possede-t-il un cube ? {}".format(mot, est_sans_cube(mot)))

    
if(__name__ == "__main__") :
    main()
