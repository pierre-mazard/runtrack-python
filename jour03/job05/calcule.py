# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:01:28 2023

@author: Mazard Pierre

Programme d'introduction aux fonctions
"""

#Importation de fonctions externes (librairies) :
    
#Définition locale de fonctions : 

def calcule (num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur ! Division par zéro"
    elif operator == '*':
        return num1 * num2
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur ! Division par zéro"
    else:
        return "Erreur ! Opérateur non valide "
 
#Déclaration des variables : 
    
#Corps principal du programme : 
    
print (calcule(20, '+', 10))
print (calcule(30, '-', 8))
print (calcule(60, '/', 3))
print (calcule(17, '/', 0))
print (calcule(5, '*', 36))
print (calcule(8, '%', 6))
print (calcule(9, '%', 0))
print (calcule(6, 'b', 8))