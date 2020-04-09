#Input n = 5 banyak siswa beserta nilai, kemudian urutkan 3 terbesar
mahasiswa = []
for i in range(0,5):
    nama = input(f"Nama Mahasiswa {i+1} = ")
    nilai = float(input(f'Nilai Mahasiswa {i+1} = '))
    x = [nama, nilai]
    mahasiswa.append(x)
mahasiswa.sort()
for i in range (0,3):
    print(f'Rank {i+1} = {mahasiswa[i][0]} : {mahasiswa[i][1]}')

  