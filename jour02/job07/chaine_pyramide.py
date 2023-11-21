chaine = "abcdefghijklmnopqrstuvwxyz" * 10

i = 0
j = 1
while i < len(chaine):
    print(chaine[i:i+j])
    i += j
    j += 1