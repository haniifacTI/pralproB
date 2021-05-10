""" SMA XYZ angkatan 100 sedang mengadakan voting pemilihan destinasi
liburan kenaikan kelas. Angkatan 100 terbagi menjadi 8 kelas.
Akan ada 3 tempat tujuan liburan yang terdapat pada voting.
Buatlah program untuk menghitung 3 hasil voting terbanyak dan mencari kelas mana saja yang belum memilih
tempat liburan agar panitia dapat dengan mudah mengetahui kelas mana yang belum memilih

Tujuan liburan : tidak ada batasan, pilih 3 terbanyak dari tujuan yang ada
Kelas : Kelas diberi nama A sampai H  """

#Input
#Tujuan liburan, voting, kelas mana saja yang memilih
#Proses
#Mengambil hasil voting 3 terbanyak, mencari kelas mana yang belum memilih dari 3 hasil voting
#Output
#kelas belum memilih destinasi liburan

tujuan = input("Masukkan tujuan liburan: ").split()
voting = list()
for destinasi in tujuan:
    suara = int(input(f"Berapa kelas yang memilih tujuan {destinasi}: "))
    voting.append(suara)

tujuan_final = list()
counter = 0
while True:
    terbanyak = max(voting)
    indeks = voting.index(terbanyak)
    tujuan_final.append(tujuan[indeks])
    voting.remove(terbanyak)
    tujuan.remove(tujuan[indeks])
    counter +=1
    if counter == 3:
        break

kelas = {'A','B','C','D','E','F','G','H'}

tujuan1 = set(input(f"Kelas mana yang memilih liburan {tujuan_final[0]}: ").split())
tujuan2 = set(input(f"Kelas mana yang memilih liburan {tujuan_final[1]}: ").split())
tujuan3 = set(input(f"Kelas mana yang memilih liburan {tujuan_final[2]}: ").split())

belumpilih = kelas-(tujuan1|tujuan2|tujuan3)
print("Kelas yang belum memilih tujuan: ",end="")
for i in belumpilih:
    print(i,end=' ')
