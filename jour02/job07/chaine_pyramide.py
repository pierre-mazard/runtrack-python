#Récupérer et afficher des caractères en suite pyramidale à partir d'un chaîne.

#Variables

chaine = "abcdefghijklmnopqrstuvwxyz" * 10
n = 1
i = 0

#boucle

while i < len(chaine):
    print(chaine[i:i+n])
    i += n
    n +=1