
"""
Created on Wed Nov 23 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def my_long_word (chiffre_entier, chaine):
    words = chaine.split()
    long_words = []
    for word in words:
        count = sum(1 for char in word)
        if count > chiffre_entier:
            long_words.append(word)
    return long_words
    

#Déclaration des variables : 

#Corps principal du programme : 

print(my_long_word (5, "Je suis gentil et j'aime le chocolat"))
print(my_long_word (4,"La peur est le chemin vers le côté obscur, la peur mène à la colère, lacolère mène à la haine, la haine mène à la souffrance"))