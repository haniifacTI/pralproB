
""" Anda diminta oleh guru anda untuk membuatkan aplikasi untuk
lomba cerdas cermat disekolahmu. Jumlah soal yang diberi ada 5
dengan tipe soal pilihan ganda. 
ATURAN : 
a. Bila berhasil menjawab 1 pertanyaan, mendapat poin 1
b. Bila memilih opsi pass/menyerah, diberikan poin 0
c. Bila salah menjawab, peserta akan dikenakan -1 poin
d. Peserta dinyatakan menang jika berhasil menjawab minimal
   3 buah soal

SOAL 1. Mengapa airmata rasanya asin? JWB: Karena mengandung elektrolit
SOAL 2. Mengapa langit berwarna biru? JWB: Karena mata manusia lebih peka terhadap warna biru
SOAL 3. Siapa presiden ke-4 Indonesia? JWB: Abdurrahman Wahid
SOAL 4. Berapa hasil dari 8/2(2+2)? JWB: 16
SOAL 5. Rendang merupakan makanan khas dari? JWB: Sumatera Barat."""

#CODE
nama = str(input("Nama: "))
asal = str(input("Asal Sekolah: "))
poin = 0
print("Soal 1")
print("Mengapa airmata rasanya asin?")
print("1. Karena mengandung elektrolit\n2. Karena sedang sedih\n3. Lewati")
jwb1=int(input("Jawab dengan menggunakan angka: "))
if jwb1==1:
    poin += 1
elif jwb1 == 2:
    poin = poin - 1
else:
    pass
print("Soal 2")
print("Mengapa langit berwarna biru?")
print("1. Karena di langit tidak ada apa-apa\n2. Karena mata manusia lebih peka terhadap warna biru.\n3. Lewati")
jwb2=int(input("Jawab dengan menggunakan angka: "))
if jwb2==2:
    poin += 1
elif jwb2 == 1:
    poin = poin - 1
else:
    pass
print("Soal 3")
print("Siapa presiden ke-4 Indonesia?")
print("1. BJ. Habibie\n2. Abdurrahman Wahid\n3. Lewati")
jwb3=int(input("Jawab dengan menggunakan angka: "))
if jwb3==2:
    poin += 1
elif jwb3 == 1:
    poin = poin - 1
else:
    pass
print("Soal 4")
print("Berapa hasil dari 8/2(2+2)?")
print("1. 16\n2. 1\n3. Lewati")
jwb4=int(input("Jawab dengan menggunakan angka: "))
if jwb4==1:
    poin += 1
elif jwb4 == 2:
    poin = poin - 1
else:
    pass
print("Soal 5")
print("Rendang merupakan makanan khas dari?")
print("1.Sumatra Barat\n2. Jawa Tengah\n3. Lewati")
jwb5=int(input("Jawab dengan menggunakan angka: "))
if jwb4==1:
    poin += 1
elif jwb4 == 2:
    poin = poin - 1
else:
    pass

if poin >=3:
    print(f"Selamat {nama} dari {asal}, anda memenangkan Lomba Cerdas Cermat!")
    print(f"Poin anda: {poin}")
else:
    print(f"Maaf {nama} dari {asal}, anda belum lulus Lomba Cerdas Cermat!")
    print(f"Poin anda: {poin}")