""" Ibrahim ingin mengirimkan pesan kepada temannya,
tetapi ia tidak ingin teman lainnya tahu tentang isi
pesan tersebut. Bantulah ia dalam merancang pesan
enkripsi dan buatlah agar bisa di dekripsi (caesar encryption) """

#CODE
print("===== PROGRAM ENKRIP/DEKRIP PESAN =====")
print("1. Enkrip\n2. Dekrip")
pilih = int(input("Pilih dari kedua diatas: "))

pesan = input("Masukkan pesan: ")
geser = int(input("Geser sebanyak: "))
pesan = pesan.lower()

listHuruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']
if pilih == 1:
    # ENKRIPSI
    pesanhasilenkrip = ""
    for i in range(len(pesan)):
        if pesan[i] == ' ':
            pesanhasilenkrip = pesanhasilenkrip + " "
            continue
        enkripsi = (listHuruf.index(pesan[i]) + geser)%26
        pesanhasilenkrip = pesanhasilenkrip + listHuruf[enkripsi]
    print(f"Pesan = {pesanhasilenkrip}")
elif pilih == 2:
    #DEKRIPSI
    pesanhasildekrip = ""
    for i in range(len(pesan)):
        if pesan[i] == ' ':
            pesanhasildekrip = pesanhasildekrip + " "
            continue
        dekripsi = (listHuruf.index(pesan[i]) - geser)%26
        pesanhasildekrip = pesanhasildekrip + listHuruf[dekripsi]
    print(f"Pesan = {pesanhasildekrip}")
else:
    print("Pilihan anda tidak ada dalam pilihan diatas.")
