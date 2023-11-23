
"""
Created on Wed Nov 23 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def produit_intervalle (L):
    produit = 1
    for i in L:
        if 25 <= i <= 90:
            produit *= i
    return produit
  
        
#Déclaration des variables : 
 
L = [8, 24, 27 ,48, 2, 16, 9, 102, 7, 84, 91]
#Corps principal du programme : 
print (L)
print(f"Le produit des valeurs de la liste comprises dans l'intervalle [25, 90] est égal à : {produit_intervalle(L)}")