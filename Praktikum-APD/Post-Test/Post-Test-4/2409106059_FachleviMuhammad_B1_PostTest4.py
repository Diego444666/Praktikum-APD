import os

os.system('cls')

username = "Fachlevi Muhammad"
password = "059"

for percobaan in range(3):
    print("Login")
    input_username = input("Masukkan Username: ")
    input_password = input("Masukkan Password: ")

    if input_username != username:
        print("Username salah.")
    elif input_password != password:
        print("Password salah.")
    else:
        break

    os.system('cls')

else:
    print("Anda telah salah memasukkan Username/Password sebanyak 3 kali.")
    exit()


while True:
    os.system('cls')
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
        input("Tekan Enter untuk kembali ke menu...")

    elif pilihan == '2':
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas = (r * r) * 3.14
        print(f"Luas lingkaran adalah: {luas}")
        input("Tekan Enter untuk kembali ke menu...")

    elif pilihan == '3':
        a = float(input("Masukkan panjang alas: "))
        b = float(input("Masukkan panjang sisi miring: "))
        keliling = 2 * (a + b)
        print(f"Keliling jajar genjang adalah: {keliling}")
        input("Tekan Enter untuk kembali ke menu...")

    elif pilihan.lower() == 'n':
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        input("Tekan Enter untuk kembali ke menu...")


