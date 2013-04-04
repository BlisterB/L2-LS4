#!/usr/bin/env python3
import sys

def celsius(nombre) :
    return (nombre-32)*(5//9)

def fahrenheit(nombre) :
    return nombre*(9//5)+32

def metre(nombre) :
    return nombre//1.0936

def yard() :
    return nombre*1.0936

def help() :
    print("Convertit :\Celsius <=> Fahrenheit\nMetre <=> Yard")

def gestionParametre() :
    #On va supposer que les arguments sont dans le bon format
    #On définit les mesures
    nombre = int(sys.argv[4])
    if sys.argv[3] == "Celsius" :
        ancienSysteme = "Celsius"
        nouveauSysteme = "Farhenheit"
        nombreConverti = fahrenheit(nombre)
    elif sys.argv[3] == "Fahrenheit" :
        print("CAAAAACAAAAAAA")
        ancienSysteme = "Farhenheit"
        nouveauSysteme = "Celsius"
        nombreConverti = celsius(nombre)
    elif sys.argv[3] == "Metre" :
        ancienSysteme = "Metre"
        nouveauSysteme = "Yard"
        nombreConverti = yard(nombre)
    elif sys.argv[3] == "Yard" :
        ancienSysteme = "Yard"
        nouveauSysteme = "Metre"
        nombreConverti = metre(nombre)
    else :
        print("Systeme non reconu")
        sys.exit()
    print("{0} {1} ---> {2} {3}".format(nombre, ancienSysteme, nombreConverti, nouveauSysteme)) 

if __name__ == '__main__' :
    if len(sys.argv) == 5 : 
        gestionParametre()
    else :
        print("Erreur d'arguments")
