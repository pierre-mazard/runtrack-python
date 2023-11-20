# Script qui détermine si une chaîne contient ou non le caractère "e".


#Message d'acceuil.
print ("""

        Script qui détermine si le caractère <<e>> est présent dans une chaîne.

""")

#Attribution des variables.
chaine = str(input("Entrez une chaîne de caractères : "))

#Recherche du caractère "e" dans le châine.
def e_present(chaine):
    if 'e' in chaine:
        return """  => La chaîne contient le caractère 'e'.
"""

    else:
        return "  => La chaîne ne contient pas le caractère 'e'."

print ((e_present)(chaine))

