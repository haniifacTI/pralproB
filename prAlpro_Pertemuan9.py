""" Sinde ingin membuat daftar urutan pemesanan kue buatannya,
dikarenakan antrean yang panjang, ia membutuhkan program
pengingat pelanggannya. Isi pengingat terdapat nama orang
dan harga pembayaran kue nya. Bantulah Sinde dalam masalah ini
Gunakan Error Handling minimal satu agar Sinde tidak kebingungan
Saat terjadi error dalam program """

pelanggan = []
harga = []

while True:
    print("========== Selamat Datang! ==========")
    print("1. Tambahkan daftar pelanggan dan harga kue")
    print("2. Lihat daftar pelanggan dan harga kue")
    print("3. Keluar Program")


    try:
        pilih = int(input("Masukkan pilihan anda: "))
    except ValueError:
        print("ERROR! Anda memasukkan bukan angka!")
        break

    if pilih <=0 or pilih >= 4:
        print("ERROR! Anda memasukkan selain pilihan di atas!")
        break
    elif pilih == 1:   # Jika memilih pilihan 1

        nama = input("Masukkan nama pelanggan: ")
        pelanggan.append(nama)
        rp = int(input("Masukkan harga: Rp"))
        harga.append(rp)
        print()

    elif pilih == 2:   # Jika memilih pilihan 2
        print("\n DAFTAR PELANGGAN DAN HARGA KUE")
        print("=================================")

        for i in range(len(pelanggan)):
            print(f"   {pelanggan[i]}      {harga[i]}")
        print()

    else:              # Jika memilih pilihan 3
        print("Terimakasih!")
        break
