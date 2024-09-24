
print("========================================")
print(" Menu Program Menghitung Luas/Keliling Bangun Datar")
print("========================================")
print("1. Keliling Segitiga")
print("2. Luas Lingkaran")
print("3. Keliling Jajar Genjang")
print("N. Keluar Program")
pilihan = input("Masukkan nomor pilihan menu: ")

if pilihan == '1':
    a = float(input("Masukkan panjang sisi pertama: "))
    b = float(input("Masukkan panjang sisi kedua: "))
    c = float(input("Masukkan panjang sisi ketiga: "))
    keliling = a + b + c
    print(f"Keliling segitiga adalah: {keliling}")
    
elif pilihan == '2':
    r = float(input("Masukkan jari-jari lingkaran: "))
    luas = (r * r) * 3.14
    print(f"Luas lingkaran adalah: {luas}")
    
elif pilihan == '3':
    a = float(input("Masukkan panjang alas: "))
    b = float(input("Masukkan panjang sisi miring: "))
    keliling = 2 * (a + b)
    print(f"Keliling jajar genjang adalah: {keliling}")
    
elif pilihan.lower() == 'n':
    print("Terima kasih telah menggunakan program ini.")
    
else:
    print("Pilihan tidak valid, silakan coba lagi.")



