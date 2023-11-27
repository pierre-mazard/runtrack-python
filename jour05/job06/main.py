# -*- coding: utf-8 -*-
"""
Created on Nov 27 2023

@author: Mazard Pierre


"""


#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 

def calcul_distance(nombre_de_marche,hauteur_des_marches):
   distance_semaine = (aller_retour_par_jour)*(semaine)*(nombre_de_marche)*((hauteur_des_marches)/100) 
   return distance_semaine

#Déclaration des variables : 
  
semaine = int(7)

aller_retour_par_jour = int(10)

nombre_de_marche = int(input(f"""
De combien de marches est composé le phare ? """))
                                   
hauteur_des_marches = float(input(f"""
Quelle est la hauteur des marches en cm ? """))

#Corps principal du programme : 


print (f"""

Pour {nombre_de_marche} marches de {hauteur_des_marches} cm, le gardien parcout {calcul_distance(nombre_de_marche, hauteur_des_marches)} m par semaine.""")
