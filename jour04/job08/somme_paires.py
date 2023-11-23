
"""
Created on Wed Nov 23 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def somme_paires (L):
    somme = sum(i for i in L if i % 2 == 0)
    return somme
        
#Déclaration des variables : 
 
L = [8, 24, 27 ,48, 2, 16, 9, 7, 84, 91]

#Corps principal du programme : 
print (L)
print(f"La somme de toutes les valeurs paires la liste est : {somme_paires(L)}")