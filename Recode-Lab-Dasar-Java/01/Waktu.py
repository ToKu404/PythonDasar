detik = int(input('Masukkan Total Detik = '))
jam = detik/3600
detik = detik%3600
menit = detik/60
detik = detik%60
print("%02d:%02d:%02d"%(jam,menit,detik))