#!/usr/bin/env python3

class CompteEpargneTemps() :
    """Une classe gérant des comptes epargnes"""
    nb_employes = 0

    def __init__(self, nom="Michel", solde=0) :
        self.nom = nom
        self.solde = solde
        CompteEpargneTemps.nb_employes += 1

    def ajout(self, n) :
        self.solde += n
        
    def afficher(self) :
        print("Nom : {}\nSolde : {} heures".format(self.nom, self.solde))

    def nombre() :
        print("Nous denombrons {} employés".format(CompteEpargneTemps.nb_employes))

def main() :
    client = CompteEpargneTemps("Rachid")
    client = CompteEpargneTemps("Dalida")
    client.ajout(50)
    client.afficher()
    CompteEpargneTemps.nombre()
    

if(__name__ == "__main__") :
    main()
