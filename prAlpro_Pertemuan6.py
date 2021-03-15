""" Ani mendapatkan data tunggal yang ingin diurutkan dari
data terkecil hingga data terbesar. Buatlah program Untuk
mengurutkan data dari terkecil hingga terbesar """

#CODE
angka = input("Masukkan angka: ")
listAngka = angka.split()

#Mengubah string ke int
for i in range(len(listAngka)):
    listAngka[i] = int(listAngka[i])

#algoritma bubble sort
for ulang in range(len(listAngka)):
    for i in range(len(listAngka)-ulang-1):
        if listAngka[i] > listAngka[i+1]:
            simpan = listAngka[i]
            listAngka[i] = listAngka[i+1]
            listAngka[i+1] = simpan

print(listAngka)