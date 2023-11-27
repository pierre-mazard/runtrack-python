# -*- coding: utf-8 -*-
"""
Created on Nov 27 2023

@author: Mazard Pierre


"""

print ("""Voici un programme affichant un tapis de n+1.
       """)
#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 
  
def tapis (n):
    print (bordure_haut_bas)
    i = 0
    while i < (n+1):
        print("|"+"#"*(n-i)+" "+"#"*(1*i)+"|")
        i += 1
    print (bordure_haut_bas)
#Déclaration des variables : 
    
n = int(input("Entrez la valeur n de la taille du tapis :  "))
bordure_haut_bas = ('+' + '-' * (n + 1) + '+')

#Corps principal du programme : 

tapis (n)
