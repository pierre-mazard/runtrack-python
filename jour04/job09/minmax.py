
"""
Created on Wed Nov 23 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def minmax (L):
    valeur_max = max(L)
    valeur_min = min(L)
    return valeur_min, valeur_max
  
        
#Déclaration des variables : 
 
L = [8, 24, 27 ,48, 2, 16, 9, 102, 7, 84, 91]
valeur_min, valeur_max = minmax(L)
#Corps principal du programme : 
print (L)
print(f"La valeur max de la liste est : {valeur_max} ") 
print(f"La valeur min de la liste est : {valeur_min} ") 