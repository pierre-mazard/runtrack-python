#Evaluation triangle


#Message d'acceuil
print ("""
Voici un programme permettant de déterminer s'il est possible de former un triangle
avec trois longueurs, et indiquant la nature de ce triangle.
""")

#variables
a = float(input("""
Entrez la longeur de a : """))
print ("""
       Longeur de""",(a) , "cm enregistrée.")
b = float(input("""
Entrez la longueur de b : """))
print ("""
       Longeur de""",(b) , "cm enregistrée.")
c = float(input(""""
Entrez la longueur de c : """))
print ("""
       Longeur de""",(c) , "cm enregistrée.")

# Vérifie si ces longueurs peuvent former un triangle
if a + b > c and a + c > b and b + c > a:
    print("""
Il est possible de former un triangle avec ces trois longeurs.
""")
    
    # Vérifie si le triangle est équilatéral
    if a == b == c:
        print("""
              => Le triangle est équilatéral.""")
    # Vérifie si le triangle est isocèle
    elif a == b or a == c or b == c:
        # Vérifie si le triangle est rectangle
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("""
                  => Le triangle est rectangle et isocèle.""")
        else:
            print("""
                  => Le triangle est isocèle.""")
    # Vérifie si le triangle est rectangle
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("""
              => Le triangle est rectangle.""")
    else:
        print("""
              => Le triangle est quelconque.""")
else:
    print("""
          Ces longueurs ne peuvent pas former un triangle!""")