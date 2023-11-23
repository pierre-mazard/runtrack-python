
"""
Created on Wed Nov 23 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 
  
def ordre_croissant(L):  
    while L:
        min = L[0]
        for i in L:
            if i < min:
                min = i
        L2.append(min)
        L.remove(min)
    print (f"""
Liste triée : 

{L2}""")

    
#Déclaration des variables : 
 
L = [58, 3, -29, 321, 12, 5, -7, 109, 84, -65]
L2 = []

#Corps principal du programme : 
print (f"""
Liste non triée : 

{L}""")
ordre_croissant(L)