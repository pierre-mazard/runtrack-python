# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:01:28 2023

@author: Mazard Pierre

Programme d'introduction aux fonctions
"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def signe (nombre):
    if nombre > 0:
        print (f"Le nombre {nombre} est positif.")
    elif nombre < 0:
        print (f"Le nombre {nombre} est négatif.")
    else :
        print (f"Le nombre {nombre} est nul.")
 
#Déclaration des variables : 
    
#Corps principal du programme : 

signe(1)
signe(45)
signe(-5)
signe(-28)
signe(0)    
