
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
        L2.append(int(min + 0.5))
        L.remove(min)
    print (f"""
Liste triée : 

{L2}""")

    
#Déclaration des variables : 
 
L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
L2 = []

#Corps principal du programme : 
print (f"""
Liste non triée : 

{L}""")
ordre_croissant(L)