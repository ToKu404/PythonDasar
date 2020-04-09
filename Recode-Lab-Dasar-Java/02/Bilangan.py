genap = 0
ganjil = 0
positif = 0
negatif = 0

try:
    bil1 = int(input())
    bil2 = int(input())
    bil3 = int(input())
    bil4 = int(input())
    bil5 = int(input())
    kumpulan = [bil1,bil2,bil3,bil4,bil5]
    for i in kumpulan:
        if(i%2 is 0):
            genap+=1
        elif(i%2 is not 0):
            ganjil+=1
        if(i>0):
            positif+=1
        elif(i<0):
            negatif+=1
except ValueError:
     print('Inputan Tidak Valid')

print("%d Bilangan Ganjil"%ganjil)
print("%d Bilangan Genap"%genap)
print("%d Bilangan Positif"%positif)
print("%d Bilangan Negatif"%negatif)

