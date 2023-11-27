# -*- coding: utf-8 -*-
"""
Created on Nov 27 2023

@author: Mazard Pierre


"""

print ("""Voici un programme affichant un triangle en fonction de la hauteur entrée.
       """)
#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 
  
def draw_triangle(height):
    for i in range(height):
        espaces = ' ' * (height - i - 1)
        if i == 0:
            cotés = '/\\'
        elif i == height - 1:
            cotés = '/' + '_' * (2 * i) + '\\'
        else:
            cotés = '/' + ' ' * (2 * i) + '\\'
        print(espaces + cotés)

    
#Déclaration des variables : 
    
height = int(input("""
Entrez la valeur de la hauteur désirée : """))


#Corps principal du programme : 

draw_triangle(height)
