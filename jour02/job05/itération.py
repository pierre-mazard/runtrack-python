#Programme qui itère le snombres de 1 à 100.
#Affichant Fizz pour les mutliples de 3.
#Affichant Buzz pour les mutliples de 5.
#Affichant FizzBuzz pour les multiples de 3 et 5.

for i in range(1, 101):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)