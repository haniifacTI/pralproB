# Haniif Ahmad Candraputra
# NIM 71200660
# UNIVERSITAS KRISTEN DUTA WACANA

""" Rahardian ingin memasang ubin berbentuk persegi dirumah baru nya. 
Karena ia tidak mempunyai waktu untuk menghitung berapa banyak 
ubin yang ia perlukan agar rumahnya terpasang ubin, ia meminta tolong
kepada kamu untuk membuatkan aplikasi untuk menghitung butuh berapa banyak
ubin yang harus Rahardian beli dan uang yang perlu ia siapkan """

# CODE
luas_rumah = int(input("Luas rumah dalam meter pesegi : "))
sisi_ubin = int(input("Sisi ubin dalam cm : "))
harga_ubin = int(input("Harga ubin perbuah : "))
jumlah_ubin = 1

while jumlah_ubin * sisi_ubin**2 < luas_rumah * 10000:
    jumlah_ubin = jumlah_ubin + 1
    if jumlah_ubin * sisi_ubin**2 >= luas_rumah * 10000:
        print("===============\nJumlah ubin yang dibutuhkan",jumlah_ubin)

totalHarga_ubin = harga_ubin * jumlah_ubin
print(f"Uang yang diperlukan untuk membeli semua ubin Rp{totalHarga_ubin}")