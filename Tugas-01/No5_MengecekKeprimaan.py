#Mengecek Ke Primaan Sebuah Bilanhan
N = int(input("N = "))
for i in range(2,(N//2)+1):
    if(N%i==0):
        print("Bukan Bilangan Prima")
        break
else:
    print("Bilangan Prima")