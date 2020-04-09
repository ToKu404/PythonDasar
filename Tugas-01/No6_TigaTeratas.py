#Input n = 5 banyak siswa beserta nilai, kemudian urutkan 3 terbesar
mahasiswa = [[input(f"Nama Mahasiswa = "),float(input(f'Nilai Mahasiswa = '))] for i in range (5)]
mahasiswa.sort(key = lambda x:x[1], reverse = True)
for i in range (0,3):
    print(f'Rank {i+1} = {mahasiswa[i][0]} : {mahasiswa[i][1]}')

  