# -*- coding: utf-8 -*-
"""
Created on Nov 27 2023

@author: Mazard Pierre


"""

print ("""
Voici un programme permettant de chiffrer un message.
       """)
#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 


def crypt(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_decale = ''
    
    for lettre in message:
        if lettre in alphabet:
            index = (alphabet.index(lettre) + decalage) % len(alphabet)
            message_decale += alphabet[index]
        else:
            message_decale += lettre
    
    return message_decale


#Déclaration des variables :  

message = str(input("""
Quel est le message à crypter : 
=> """))

decalage = int(input("""
Quel décalage souhaitez vous appliquer à votre message ? 
=> """))


#Corps principal du programme : 

print (f"""
Voici le résulat :
    
=> {crypt(message, decalage)}""")