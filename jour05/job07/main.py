# -*- coding: utf-8 -*-
"""
Created on Nov 27 2023

@author: Mazard Pierre


"""

#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 
  
def arrondir_notes(notes):
    notes_arrondies = []
    for notes in notes:
        if notes < 40:
            notes_arrondies.append(notes)
        else:
            reste = notes % 5
            if reste >= 3:
                notes += 5 - reste
            notes_arrondies.append(notes)
    return notes_arrondies
            

    

#Déclaration des variables : 

notes = [83, 82, 100, 25, 4, 75, 89, 96, 23, 14, 54, 62, 13, 21, 24, 84, 66, 71, 39, 46, 45, 92]
notes_arrondies = arrondir_notes(notes)
#Corps principal du programme : 

print(notes_arrondies)