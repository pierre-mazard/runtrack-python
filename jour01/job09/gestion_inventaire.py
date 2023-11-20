#Script gestion d'inventaire.

#Attribution des variables
nom_produit = "Orchidée Dendrobium Berry Oda"
prix_unitaire = 25.00
quantite_stock = 35

#Informations produit
print (f"Nom du produit : {nom_produit}")
print (f"Prix unitaire : {prix_unitaire}€")
print (f"""Quantité en stock : {quantite_stock} pièces
""")

#Mise à jour du stock
maj_stock = int(input("Quantité de produits à ajouter au stock actuel :"))
quantite_stock += maj_stock

#Augmentation du prix suite à l'inflation (augmentation de 10%)
prix_unitaire *= 1.1
prix_unitaire_arrondi = round(prix_unitaire * 100) / 100


#Affichage des informtions produit mise à jour
print (f"""
Nom du produit : {nom_produit}""")
print (f"Mise à jour du prix suite à une augmentation de 10% : {prix_unitaire_arrondi}€")
print (f"Quantité actuelle : {quantite_stock} pièces")
