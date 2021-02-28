""" Beni bekerja sebagai perawat kolam ikan. Ketika bekerja, Beni kerepotan untuk 
menentukan berapa liter air yang dibutuhkan dan berapa lama untuk kolam terisi.
Asumsi bahwa keran mengeluarkan air 5 liter per menit, bantulah Beni untuk mencari
berapa liter air yang diperlukan dan berapa lama pengisian kolam. """

#CODE
def volumeAir(p,l,t):
    vol = p*l*t/1000
    return vol

def waktu(vol):
    waktu = vol/5
    return waktu

print("==== HALO BENI, SILAKAN LANJUT KE PROGRAM ====")
panjang = int(input("Masukkan panjang kolam : "))
lebar = int(input("Masukkan lebar kolam : "))
tinggi = int(input("Masukkan kedalaman kolam : "))

volumeKolam = volumeAir(panjang,lebar,tinggi)
print("==== HASIL KALKULASI ====")
print(f"Air yang dibutuhkan untuk mengisi kolam sebanyak {volumeKolam} Liter")
print(f"Waktu untuk mengisi kolam ikan sampai penuh adalah {waktu(volumeKolam)}")