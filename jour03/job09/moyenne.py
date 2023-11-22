# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:01:28 2023

@author: Mazard Pierre

Programme d'introduction aux fonctions
"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def moyenne (note1, note2, note3):
    return (note1 + note2 + note3) / 3
    
#Déclaration des variables : 
note1 = float(input(f"Saisir la première note : ")) 
note2 = float(input(f"Saisir la seconde note :"))
note3 = float(input(f"Saisir la troisième note :"))
moyenne_etudiant = moyenne (note1, note2, note3)
   
#Corps principal du programme : 

if 15 <= moyenne_etudiant <= 20:
    print ("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print ("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print ("Elève moyen")
elif 0<= moyenne_etudiant <= 7:
    print ("Elève devant faire des efforts")
