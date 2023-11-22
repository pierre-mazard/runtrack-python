# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:01:28 2023

@author: Mazard Pierre

Programme d'introduction aux fonctions
"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def time_to_text (minutes):
    heures = int(minutes / 60)
    minutes_restantes = int(minutes % 60)
    return f"{heures} heures et {minutes_restantes} minutes"   
    
#Déclaration des variables : 
    
#Corps principal du programme : 

print(time_to_text(180))    
print(time_to_text(25))
print(time_to_text(60))
print(time_to_text(3653))
print(time_to_text(43))
