#Menentukan banyak bilangan negatif dalam sebuah List
list = [0,-4,3,2,-5,-4,3]
negatifList = [i for i in range(0,len(list)) if list[i]<0]
print(f'Banyaknya Bilangan Negatif = ',len(negatifList))



