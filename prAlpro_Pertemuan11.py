""" Indah sedang melakukan pencatatan pekerjaan orangtua
mahasiswa di universitas tempat ia belajar, Dikarenakan 
banyaknya orangtua mahasiswa yang didata oleh Indah, ia lupa
apakah sudah memasukkan jenis pekerjaan yang sama sebelumnya atau
belum. bantulah indah dalam mendata jenis pekerjaan orangtua """

#1 Tentara PNS Dokter
#2 Freelancer Dokter Freelancer

""" #Input
jenis pekerjaan
#Proses
bila sudah terdapat jenis pekerjaan sama tidak perlu ditambah lagi
dapat melihat jenis pekerjaan
#Output
isi tuple dari pekerjaan  """

jenisPekerjaan = tuple()
while True:
    print("=====Program Pendataan Pekerjaan Orangtua=====")
    print("1. Tambah Pekerjaan\n2. Lihat Pekerjaan\n3. Keluar")
    pilih = int(input("Masukkan pilihan : "))
    if pilih == 1:
        while True:
            pekerjaan = input("Masukkan Jenis Pekerjaan (0 untuk keluar) : ")
            if pekerjaan == "0":
                print()
                break
            elif pekerjaan not in jenisPekerjaan:
                jenisPekerjaan = list(jenisPekerjaan)
                jenisPekerjaan.append(pekerjaan)
                jenisPekerjaan = tuple(jenisPekerjaan)
            else:
                print("Jenis pekerjaan sudah ada.\n")
    if pilih == 2:
        print("Jenis Pekerjaan yang terdaftar : ")
        nomer = 1
        for jenis in jenisPekerjaan:
            print(f"{nomer}. {jenis}")
            nomer +=1
    elif pilih == 3:
        print("Program Berhenti")
        break