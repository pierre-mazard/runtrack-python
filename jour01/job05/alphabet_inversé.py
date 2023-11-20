#Script qui affiche l'alphabet à l'envers

print ("Voici un script qui liste l'aphabet à l'envers.")

for i in reversed(range(26)):
        print(chr(i + ord('A')))
