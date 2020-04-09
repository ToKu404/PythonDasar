import math
high = float(input("Ketinggian Menara = "))
alfa = float(input("Sudut Elevasi Terhadap Ujung Depan Kapal = "))
beta = float(input("SUdut Elevasi Terhadap Ujung Belakang Kapal = "))
if (alfa<90 and beta<alfa):
    print('Panjang Kapal %.1f m'%((math.tan(alfa*math.pi/180))*high-(math.tan(beta*math.pi/180))*high))
else:
    print('Maaf input anda salah')