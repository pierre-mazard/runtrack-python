# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:01:28 2023

@author: Mazard Pierre

Programme d'introduction aux fonctions
"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def lang (langage):
    if langage == str("JavaScript"):
        print ("Tu es unn développeur web.")
    elif langage == str("python"):
        print ("Tu es un développeur IA.")
    elif langage == str("java"):
        print ("Tu es un développeur logiciel.")
    else :
        print ("Tu n'est pas développeur.")
 
#Déclaration des variables : 
    
#Corps principal du programme :

lang("JavaScript")
lang("python")
lang("java")
lang("salut")