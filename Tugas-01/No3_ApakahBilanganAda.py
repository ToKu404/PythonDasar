#Mengecek Apakah Bilangan X terdapat dalam List
list = [0,1,2,3,4,5]
x = int(input("X = "))

if x in list:
    print(f'{x} ada di list')
else:
    print(f'{x} tidak ada di list')