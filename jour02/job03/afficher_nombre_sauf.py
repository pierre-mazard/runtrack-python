# Affichage des nombres de 0 à 100 compris sauf 26, 37, 88.

#Variable 
 
nombres = range(0, 100 +1)

for x in nombres:
    if x not in [26, 37, 88]:
        print(x)