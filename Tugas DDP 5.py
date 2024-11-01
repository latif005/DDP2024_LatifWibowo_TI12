#variabel list
kendaraan = ["beat karbu", "motor", 200, "pink", 2]
kendaraan.append("13jt")
kendaraan.append("matic")
kendaraan.insert(2, "honda")
print(kendaraan)

#match case
hitung_luas = int(input("""Pilih Salah Satu Angka:
 1. Hitung Luas Persergi
 2. Hitung Luas Lingkaran
 3. Hitung Luas Segitiga
 Pilih Angka;
"""))

match hitung_luas:
    case 1:
        print ("Menghitung Luas Persegi")
        sisi = int(input("Masukkan Sisi"))
        menghitung_luas_persegi = sisi **2
        print(f'Jadi luas persegi dengan sisi {sisi} cm adalah {menghitung_luas_persegi} cm^2')
    case 2: 
        print ("Menghitung Luas Lingkaran")
        jari_jari = int(input("Masukkan Jari_Jari Lingkaran"))
        phi = 3.14
        menghitung_luas_lingkaran = phi * jari_jari**2
        print (f'Jadi Luas Lingkaran dengan Jari-Jari {jari_jari} cm adalah {menghitung_luas_lingkaran} cm^2')
    case 3:
        print("Menghitung Luas Segitiga")
        alas_segitiga = int(input("Masukkan Alas Segitiga: "))
        tinggi_segitiga = int(input("Masukkan Tinggi Segitiga: "))
        menghitung_luas_segitiga = 1/2 * alas_segitiga * tinggi_segitiga
        print (f'Jadi Luas Segitiga dengan Alas {alas_segitiga} cm dan Tinggi {tinggi_segitiga} cm adalah {menghitung_luas_segitiga} cm^2')
    case _:
        print ("Tidak Valid")

