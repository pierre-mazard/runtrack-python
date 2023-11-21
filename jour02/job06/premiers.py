#Afficher les nombres premiers jus'qu'à 1000.

#Message
print (""""
Affichage des nombres premiers jusqu'à 1000.
       """)
       
#Boucle       
for x in range(2, 1001):
    nombre_premier = True
    for i in range (2, x):
        if x % i == 0:
            nombre_premier = False
            break
    if nombre_premier:
        print (x)