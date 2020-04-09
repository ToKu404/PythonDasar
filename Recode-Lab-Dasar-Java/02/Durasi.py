print('Waktu Mulai')
startHour = int(input("Jam Mulai\t:"))
startMinutes = int(input("Menit Mulai\t:"))
print('Waktu Berakhir')
endHour = int(input("Jam Berakhir\t:"))
endMinutes = int(input("Menit Berakhir\t:"))
durasi = 0
if((startHour*60+startMinutes)>(endHour*60+endMinutes)):
    durasi=(endHour*60+endMinutes)+(24*60)-(startHour*60+startMinutes)
else:
    durasi=(endHour*60+endMinutes)-(startHour*60+startMinutes)
print("Durasi Acara\n%02d:%02d"%(durasi//60,durasi%60))