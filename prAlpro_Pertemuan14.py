""" Karena telat mengumpulkan tugas, Anita dihukum untuk menghitung jumlah huruf
vokal dan konsonan yang ada pada sebuah buku/lagu. Karena hukuman nya yang tidak waras,
Anita meminta bantuan mu untuk membantu menyelesaikan tugas hukumannya. """

""" # input
teks berupa buku/lagu dalam satu baris
# proses
memilah vokal dan konsonan
menggabungkan vokal menjadi satu string dan konsonan menjadi satu string
# output
jumlah vokal dan konsonan
string vokal dan string konsonan """

import re

teks = input("Masukkan teks:\n")
print()
vokal = re.findall('[aiueoAIUEO]',teks) #Menyaring semua huruf vokal pada teks
konsonan = re.findall('[^aiueoAIUEO ,.!@-_1234567890]',teks) #Menyaring hanya huruf konsonan pada teks

string_vokal = ''
for i in vokal:
    string_vokal+=i

string_konsonan = ''
for j in konsonan:
    string_konsonan+=j

panjang_vokal = len(string_vokal)
panjang_konsonan = len(string_konsonan)

print(f'Jumlah huruf vokal pada teks = {panjang_vokal} huruf')
print(f'Jumlah huruf konsonan pada teks = {panjang_konsonan} huruf\n')

print(f'Huruf vokal yang ada pada teks:\n{string_vokal}\n')
print(f'Huruf konsonan yang ada pada teks:\n{string_konsonan}\n')
