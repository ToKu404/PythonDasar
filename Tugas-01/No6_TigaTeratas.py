#Input n = 5 banyak siswa beserta nilai, kemudian urutkan 3 terbesar
mahasiswa = [[input(f"Nama Mahasiswa = "),float(input(f'Nilai Mahasiswa = '))] for i in range (5)]
mahasiswa2 = mahasiswa[:]
#cara manual dan jika terdapat ranking yang sama maka keduanya berbagi rank
#1)sorting
for x in range(len(mahasiswa)-1,0,-1):
    for y in range (x):
        if(mahasiswa[y][1]<mahasiswa[x][1]):
            mahasiswa[y],mahasiswa[x]=mahasiswa[x],mahasiswa[y]
#2)Print
print(">> TOP 3 << ")
rank = 0
i = 0
while rank<3:
    if i<4:             #jika i sudah >4 maka indeks dari list sudah sampai akhirnya
        print(f'Rank {rank+1} = {mahasiswa[i][0]}',end="")
        i += 1
        while mahasiswa[i][1]==mahasiswa[i-1][1]: #Memeriksa mahasiswa yg nilainya sama
            print(f',{mahasiswa[i][0]}',end=" ")
            if i<4:
                i+=1
            else:
                break
        print(f': {mahasiswa[i-1][1]}')
    else:
        print(f'Rank {rank+1} = No List')
    rank+=1

#Dengan bantuan sort dan reverse dan mengabaikan bila nilai mahasiswa sama
print(50*"=")
mahasiswa2.sort(key = lambda x:x[1], reverse = True)
for i in range (3):
    print(f'Rank {i+1} = {mahasiswa2[i][0]} : {mahasiswa2[i][1]}')

  