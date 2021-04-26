""" Kamu adalah seorang programmer sistem perpustakaan didekat kampusmu
kamu diberi tugas untuk membuat program untuk menyimpan data buku perpustakaan
dan sistem pencarian agar mudah ditemukan oleh pembaca. """
#{"Kode":"", "Judul":"", "Genre":"", "Deskripsi":"", "Rating":""}

""" #Input
pilihan antara mencari atau menambah buku
#Proses
pencarian dari database berupa dictionary
menambahkan buku baru ke dalam database
#Output
======== PERPUSTAKAAN KAMPUS XYZ ========
1. Pencarian Buku
2. Tambah Daftar Buku
3. Keluar
>> Pilihan : 1
>> Masukkan kode buku : AA001
==========================
Judul           : Kemana engkau pergi
Genre           : Comedy
Deksripsi       : Kisah seorang anak yang mencari teman kecilnya yang pergi tanpa pamit.
Rating          : 8/10

======== PERPUSTAKAAN KAMPUS XYZ ========
1. Pencarian Buku
2. Tambah Daftar Buku
3. Keluar
Pilihan : 2
==========================
Masukkan Kode Buku Baru: AA003
Masukkan Judul Buku Baru: ABC
Masukkan Genre Buku Baru: Misteri
Masukkan Deskripsi Buku Baru: ABC
Masukkan Rating Buku Baru: 9/10 """

databaseBuku = [{"Kode":"AA001", "Judul":"Testing", "Genre":"None", "Deskripsi":"None", "Rating":"0/10"},
{"Kode":"AA002", "Judul":"Ketika Hujan Turun", "Genre":"Misteri", "Deskripsi":"Seorang anak yang menunggu turunnya hujan", "Rating":"10/10"}]
while True:
    print("======== PERPUSTAKAAN KAMPUS XYZ ========")
    print("1. Pencarian Buku\n2. Tambah Daftar Buku\n3. Keluar")
    pilih = int(input("Masukkan pilihan : "))

    if pilih == 1:
        kode = input("Masukkan kode buku : ")
        print("==========================")
        for buku in databaseBuku:
            if buku["Kode"] == kode:
                print("Judul\t\t:",buku["Judul"])
                print("Genre\t\t:",buku["Genre"])
                print("Deskripsi\t:",buku["Deskripsi"])
                print("Rating\t\t:",buku["Rating"])
                print()

    elif pilih == 2:
        bukuBaru = dict()
        print("==========================")
        bukuBaru["Kode"] = input("Masukkan Kode buku baru : ")
        bukuBaru["Judul"] = input("Masukkan Judul buku baru : ")
        bukuBaru["Genre"] = input("Masukkan Genre buku baru : ")
        bukuBaru["Deskripsi"] = input("Masukkan Deskripsi buku baru : ")
        bukuBaru["Rating"] = input("Masukkan Rating buku baru : ")
        databaseBuku.append(bukuBaru)
        print()

    else:
        print("Program Terhenti")
        print("Terimakasih!")
        break
