# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:01:28 2023

@author: Mazard Pierre

Programme d'introduction aux fonctions
"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def verification (nombre):
    if nombre > 0 and type(nombre) == int:
        if nombre % 2 == 0:
            print(f"Le nombre {nombre} est pair.")
        else:
            print(f"Le nombre {nombre} est impaire.")
    else:     
        print("Veuillez choisir un nombre entier positif ! ")
     
    
#Déclaration des variables : 
    
#Corps principal du programme : 
    
verification(12.5)
verification(1)
verification(158)
verification(3)
verification(0)
verification(-18)
    
    