# -*- coding: utf-8 -*-
"""
Created on Nov 27 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 
  
def my_sort(liste):
    #Initialisation du nombre de coups
    total_coups = 0
    #Parcourir les éléments de la liste
    for i in range(len(liste)):
        #Parcourir la liste du dernier élément à i + 1
        for j in range(len(liste) -1, i, -1):
            #Si élément parcouru est plus grand que celui qui le précède
            if liste[j] < liste[j -1]:
                #Echanger les éléments
                liste[j], liste[j -1] = liste[j -1], liste[j]
                #Total de coups
                total_coups += 1
    #Liste triée et nombre total de coups
    return liste, total_coups
            

#Déclaration des variables : 
liste = [4, 10, 2, 3, 1, 58, 172, 89, 84, 21, 16, 5, 12]
liste_triee, total_coups = my_sort(liste)

#Corps principal du programme : 

print(f"Liste triée : {liste_triee}")
print(f"Nombre total de coups : {total_coups}")