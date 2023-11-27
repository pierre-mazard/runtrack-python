# -*- coding: utf-8 -*-
"""
Created on Nov 27 2023

@author: Mazard Pierre


"""

print ("""Voici un programme affichant un rectangle composé de '-' et de '|'.
       """)
#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 
  
def draw_rectangle(width, height):
    print('|' + '-' * (width - 2) + '|')
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    print('|' + '-' * (width - 2) + '|')

    
#Déclaration des variables : 

width = int(input("Entrez la valeur de la largeur désirée : "))    
height = int(input("""
Entrez la valeur de la hauteur désirée : """))


#Corps principal du programme : 

draw_rectangle(width, height)
