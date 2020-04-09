klas1 = input().lower()
klas2 = input().lower()
klas3 = input().lower()
if(klas1=="vertebrado"):
    if(klas2=="ave"):
        if(klas3=="carnivoro"):
            print("aguia")
        elif(klas3=="onivoro"):
            print("pomba")
    elif(klas2=="mamifero"):
        if(klas3=="herbivoro"):
            print("vaca")
        elif(klas3=="onivoro"):
            print("homen")
elif(klas1=="invertebrado"):
    if(klas2=="inseto"):
        if(klas3=="hematofago"):
            print("pulga")
        elif(klas3=="herbivoro"):
            print("lagarta")
    elif(klas2=="anelideo"):
        if(klas3=="hematofago"):
            print("sanguessuga")
        elif(klas3=="onivoro"):
            print("minghoca")
else:
    print("Input Invalid")
