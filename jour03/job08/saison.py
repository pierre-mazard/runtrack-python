# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:01:28 2023

@author: Mazard Pierre

Programme d'introduction aux fonctions
"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def cons (type, saison):
    if type == str("fruits") and saison == str("hiver"):
        print ("Orange, mandarine et kiwi.")
    elif type == str("fruits") and saison == str("ete"):
        print ("Poire, fraise, cassis.")
    elif type == str("legume") and saison == ("hiver"):
        print ("Carotte, topinambour, endive.")
    elif type == str("legume") and saison == ("ete"):
        print ("Artichaud, aubergine, navet.")
    else:
        print ("Erreur de saisie des paramètres !")
    
    
    
#Déclaration des variables : 
    
#Corps principal du programme : 

cons ("fruits", "hiver")   
cons ("fruits", "ete")
cons ("legume", "hiver")
cons ("legume", "ete")
cons ("soleil", "nuit")