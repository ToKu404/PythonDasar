#Mengecek Faktor dari sebuah bilangan  c dan tentukan banyaknya Faktor
c = int(input("Masukkan Nilai C = "))
list = [i for i in range(1,c+1) if c%i==0]
print(f"Faktor dari {c} adalah : ",list)
print(f"Banyaknya faktor dari {c} adalah : ",len(list))