# script qui affiche les tables de multiplications de 1 à N.

#Message 

# variables
N = int(input("Entrez un nombre entier supérieur à zéro : "))

#Message d'erreur 
if N <= 0:
    print("""
          Erreur ! 
          
Veuillez entrez un nombre entier supérieur à zéro.""")

#Boucle
else:
    for i in range(1, N+1):
        print(f""""
Table de multiplication de {i}""")
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")
        