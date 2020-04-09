n = int(input())
a = 0
b = 1
hasil = 0
for i in range(0,n):
    hasil = a
    a +=b
    b = hasil
    print(hasil,end=" ")
    
