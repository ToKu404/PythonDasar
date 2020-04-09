startNumber = int(input())
endNumber = int(input())
if(endNumber<startNumber):
    repo = startNumber
    startNumber = endNumber
    endNumber  = repo

for i in range(startNumber,endNumber):
    if i == 0:
        print(i,"nol")
        continue
    if i%2==0:
        if(i>0):
            print(i," genap positif")
        else:
            print(i,"genap Negarif")
    else:
        if(i>0):
            print(i," ganjil positif")
        else:
            print(i,"ganjil Negarif")