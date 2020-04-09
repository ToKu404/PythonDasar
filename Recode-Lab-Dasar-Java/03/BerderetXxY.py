try:
    x = int(input("Jumlah Kolom = "))
    y = int(input("Sampai Angka ke = "))
    if(x<0 or y<0):
        print('Inputan Tidak Valid')
    if(y%x!=0):
        y = x*(y//x+1)        
    
    for i in range(1,y+1):
        print(i,end="\t")
        if i%x==0:
            print("")
except ValueError:
    print("Inputan tidak valid")



