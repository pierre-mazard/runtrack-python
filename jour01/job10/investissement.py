#Script de simulation d'investissement financier.

#Message d'acceuil
print ("""

          Simulation financière pour un investissement


       """)
#Attribution des vrariables
montant_initial = float(input("Veuillez entrer le montant initial de l'investissement en euros : "))
print ("""
""")
taux_rendement = float(input("Veuillez entrer la valeur du taux de rendement annuel en pourcentage :"))

#calcul du gain annuel
gain_annuel = montant_initial * (taux_rendement/100) 

#Affichage du gain annuel en fonction du taux de rendement
print ("""

"""f"Le gain annuel pour un investissement de {montant_initial} euros avec un taux de rendement annuel de {taux_rendement} % est égal à : {gain_annuel}euros.""""
""")

#Augmentation du capital de 5000 euros et du taux de 2%
print ("""
              ~Ajout de 5000 euros sur le capital et augmentation de 2% du taux de rendement annuel~
""")
montant_initial += 5000
taux_rendement =+ 2
gain_annuel = montant_initial * (taux_rendement/100)
print ("""                => """f"Le gain annuel après une agumentation du capital de 5000 euros et du taux de rendement de 2% sera de : {gain_annuel}euros.""""
""")

#Retrait de 10% du montant total et diminution du taux de rendement de 1%
print ("""
              ~Retrait de 10% du montant total et diminution du taux de rendement annuel de 1%~
""")
montant_initial -= montant_initial * 0.1
taux_rendement -= 1
gain_annuel = montant_initial * (taux_rendement/100)
print ("""              => """f"Le gain annuel apès un retrait de 10% du montant total et une diminution du taux de rendement de 1% sera de: {gain_annuel}euros.")
