
"""
Created on Wed Nov 23 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def multiples_de_3 (L):
    count = sum(1 for i in L if i % 3 == 0)
    return count
        
#Déclaration des variables : 
 
L = [8, 24, 48 ,2, 16]

#Corps principal du programme : 
print (L)
print(f"Le nombre multiple de 3 présent dans la liste est : {multiples_de_3(L)}")