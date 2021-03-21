""" Rosi ingin membuat permainan lirik lagu dimana setiap 1
kata dalam lirik akan ditambah kata baru lagi, 
# contoh:
pelangi pelangi, alangkah indahmu.
# akan berubah menjadi :
pelangi ikan pelangi, ikan alangkah ikan indahmu.
# lalu peraturan selanjutnya adalah mengganti semua huruf
vokal menjadi berurutan a i u e o
contoh :
palingu ekon palingu, ekon alingkuh ekon andihmu."""


#CODE
lirik = input("Masukkan lirik: ")
kata = input("Masukkan kata tambahan: ")

simpan1=""
pisah = lirik.split()
for i in pisah:
    if i != pisah[-1]:
        simpan1=simpan1 + i +" "+ kata + " "
    else:
        simpan1=simpan1 + i + " "

simpan2=""
vokal=["a","i","u","e","o"]
index = 0
for j in range(len(simpan1)):
    index=index%5
    if simpan1[j] in vokal:
        simpan2= simpan2 + vokal[index]
        index=index+1
    else:
        simpan2=simpan2+simpan1[j]

print(simpan2)

