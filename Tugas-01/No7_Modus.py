#Menentukan Modus dalam list
#Dengan Menggunakan mode
from statistics import mode
data1 = [3,1,3,2,1,2,2,4,5,2,1]
print("MODUS = ", mode(data1))

print(50*"=")

#Manual
#Berlaku Meski Modusnya Lebih dari 1
data2 = [2,1,2,1,4,2,1,5]
modus = []
terbanyak = 0
while len(data2)>0:
    if(data2.count(data2[0])>terbanyak):
        modus.clear()
        terbanyak = data2.count(data2[0])
        modus.append(data2[0])
    elif(data2.count(data2[0])==terbanyak):
        modus.append(data2[0])
    data2 = [value for value in data2 if value!=data2[0]]


print("MODUS = ",end=" ")
for i in range(0, len(modus)):
    print(modus[i], end=" ")
