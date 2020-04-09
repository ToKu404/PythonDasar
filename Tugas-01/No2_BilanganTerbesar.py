#Mencetak Bilangan terbesar dari sebuah List
#Menggunakan Max
list = [0,2,4,5,3,2,6,7,4,7,9,1]
print("Nilai Tertinggi = ",max(list))

#Manual
tertinggi = 0;
for i in range(0,len(list)):
    if(list[i]>tertinggi):
        tertinggi = list[i]
print("Nilai Tertinggi = ",tertinggi)