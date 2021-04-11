# Ardi ingin menggabungkan dua file notepad berisi 15 website populer
# pada sebuah negara menjadi satu file agar dia
# bisa memproses file tersebut. Kemudian bantulah ia untuk
# Mencari website paling populer di kedua negara tersebut

# Input
# file1.txt dan file2.txt
# Proses
# kita gabungkan ke dalam 1 file .txt
# lalu dicari website palin populer dari negara tersebut
# Output
# 1 file gabung
# website paling populer

# Code
final = open('final.txt','a+')
file1 = open('file1.txt','r')
file2 = open('file2.txt','r')

# Penggabungan 2 file .txt menjadi 1 file .txt
for barisfile1 in file1:
    final.write(barisfile1)
final.write('\n\n')
file1.close()

for barisfile2 in file2:
    final.write(barisfile2)
final.write('\n\n')
file2.close()
final.close()
# Perintah masukan dari user
print("========================================")
masuk = input("Apakah anda ingin menampilkan website terpopuler di masing2 negara (y/n) : ")
print("========================================")

final = open('final.txt')
# Mencari website terpopuler masing2 negara
if masuk.lower() == 'y':
    for barisfinal in final:
        if barisfinal.find('negara') != -1:
            print(f"Website terpopuler di {barisfinal[29:-1]}")
        if barisfinal.startswith('1. ') == True:
            print(barisfinal[3::])
else:
    print("Program selesai.")
final.close()
