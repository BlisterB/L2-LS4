#!/usr/bin/env python3
import string

class Personnage :
    def __init__(self, chaine) :
        chaine = chaine.replace('\n', "")
        chaine = chaine.split(",")
        self.nom = chaine[0]
        self.prenom = chaine[1]
        self.metier = chaine[2]
        self.rue = chaine[3]
        self.num = chaine[4]

    def __str__(self) :
        return "{} {} exerce la profession de {}, habite à {} rue {}".format(self.nom, self.prenom, self.metier, self.num, self.rue)

class Annuaire :
    def __init__(self, chemin) :
        self.liste = list()
        fichier = open(chemin, "r")
        for ligne in sorted(fichier) :
            self.liste.append(Personnage(ligne))
            
    def __str__(self) :
        chaine = ""
        for i in range(0, len(self.liste)) :
            chaine += self.liste[i].__str__() +"\n"
        return chaine

    def copy(self, chemin) :
        fichier = open(chemin, "w")
        for i in self.liste :
            fichier.write(i.nom + "," + i.prenom + "," + i.metier + "," + i.rue + "," + i.num + "\n")
        fichier.close()

    def liste_pages_jaunes(self, chaine) :
        """Renvoie la liste des personnages ayant le metier passé dans chaine en parametre"""
        return [personnage for personnage in self.liste if personnage.metier == chaine]

    def cherche_pages_jaunes(self
          
def main() :
    annuaire = Annuaire("liste.txt")
    print(annuaire)
    annuaire.copy("copie.txt")

if(__name__ == "__main__") :
    main()
