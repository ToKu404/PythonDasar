import math
print("[1]Bangun Datar\n[2]Bangun Ruang")
menu = int(input("> "))
if menu==1:
    print("[1]Persegi\n[2]Segitiga")
    bDatar = int(input("> "))
    if bDatar==1:
        sisi = float(input("Input Sisi = "))
        print("Luas Persegi = ",(sisi*sisi))
    elif bDatar==2:
        alas = float(input("Input Alas = "))
        tinggi = float(input('Input Tinggi = '))
        print("Luas Segitiga = ",(alas*tinggi/2))
    else:
        print("input salah")
elif menu==2:
    print("[1]Kubus\n[2]Tabung")
    bRuang = int(input("> "))
    if bRuang==1:
        sisi = float(input('Input Sisi = '))
        print("Volume Kubus = ",sisi**3)
    elif bRuang==2:
        jari2 = float(input("Input Jari-jari = "))
        tinggi = float(input("Input Tinggi = "))
        print("Volume Tabung",math.pi*(jari2**2)*tinggi)
    else:
        print('Input Salah')
else:
    print('Input salah')        