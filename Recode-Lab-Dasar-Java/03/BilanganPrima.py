bilangan = int(input("Num = "))
if bilangan<=1:
    print(bilangan,"Bukan Bilangan Prima")
else:
    for i in range(2, bilangan):
        if(bilangan%i==0):
            print(bilangan," Bukan Bilangan Prima")
            break
    else:
        print(bilangan," Bilangan Prima")
