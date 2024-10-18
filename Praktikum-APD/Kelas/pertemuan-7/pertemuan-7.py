# def hasil():
#     print("hello world" + nama)
# hasil("adi")
# hasil("adiadaw")
# hasil("adiad")

# def luas_persegi_panjang ( panjang,lebar=5):
#     luas = panjang * lebar

#     # print(f"luas{panjang}dan {lebar}adalah{luas}")
#     return  luas


# luas_persegi = luas_persegi_panjang(10,2)

# print(luas_persegi)

# nama  = "adi"

# def say_hallo():
    
#     nama = "daffa"

#     print(nama, "luar fungsi")

# print(nama, "luar fungsi")

# say_hallo()



# import os

# pengguna = [
#     ["fachlevi muhammad", "059", "admin"],
# ]

# parfumes = [
#     [1, "HMNS Essence", 300000, "Woody", "HMNS Essence memberikan aroma yang  dan strong dengan sentuhan kayu yang elegan."],
#     [2, "HMNS Orgasm", 450000, "Floral", "HMNS Orgasm memiliki aroma floral yang segar dan flirty, cocok untuk momen tender."]
# ]
# os.system('cls')

# print("Selamat datang diParfume by HMNS")
# while True:
#     print("Silakan pilih aksi:")
#     print("1. Masuk")
#     print("2. Daftar")
#     print("3. Keluar")
#     pilihan_awal = input("> ")

#     if pilihan_awal == '1':
#         for percobaan in range(3):
#             nama_pengguna = input("Nama pengguna: ")
#             kata_sandi = input("Kata sandi: ")
#             jenis_pengguna = None
#             for data in pengguna:
#                 if data[0] == nama_pengguna and data[1] == kata_sandi:
#                     print(f"Selamat datang, {nama_pengguna}!")
#                     jenis_pengguna = data[2]
#                     break
#             if jenis_pengguna:
#                 break
#             else:
#                 print(f"Nama pangguna atau kata sandi salah. Kesempatan tersisa: {2 - percobaan}")

#         if not jenis_pengguna:
#             print("Gagal masuk setelah 3 kali percobaan.")
#             continue

#         if jenis_pengguna == 'admin':
#             while True:
#                 os.system('cls')
#                 if parfumes:
#                     print("Daftar Parfum:")
#                     for parfum in parfumes:
#                         print(f"ID: {parfum[0]}, Nama: {parfum[1]}, Aroma: {parfum[3]}")
#                         print(f"Harga: {parfum[2]}, Deskripsi: {parfum[4]}")
#                 else:
#                     print("Belum ada data parfume.")

#                 print("Pilih aksi:")
#                 print("1. Tambah Parfum")
#                 print("2. Lihat Deskripsi Parfum")
#                 print("3. Ubah Parfum")
#                 print("4. Hapus Parfum")
#                 print("5. Keluar")
#                 pilihan_admin = input("> ")

#                 if pilihan_admin == "1":
#                     id_ = input("ID: ")
#                     nama = input("Nama parfum: ")
#                     harga = input("Harga: ")
#                     tipe_aroma = input("Tipe aroma: ")
#                     deskripsi = input("Deskripsi: ")
#                     parfumes.append([int(id_), nama, int(harga), tipe_aroma, deskripsi])
#                     print(f"Parfum {nama} berhasil ditambahkan!")

#                 elif pilihan_admin == "2":
#                     id_ = input("ID parfum untuk deskripsi: ")
#                     id_ = int(id_)
#                     ditemukan = False
#                     for parfum in parfumes:
#                         if parfum[0] == id_:
#                             print(f"Deskripsi Parfum {parfum[1]}: {parfum[4]}")
#                             ditemukan = True
#                             break
#                     if not ditemukan:
#                         print("Parfum tidak ditemukan.")

#                 elif pilihan_admin == "3":
#                     id_ = input("ID parfum yang ingin diubah: ")
#                     id_ = int(id_)
#                     ditemukan = False
#                     for parfum in parfumes:
#                         if parfum[0] == id_:
#                             nama_baru = input("Nama baru: ")
#                             harga_baru = input("Harga baru: ")
#                             tipe_aroma_baru = input("Tipe aroma baru: ")
#                             deskripsi_baru = input("Deskripsi baru: ")
#                             parfum[1], parfum[2], parfum[3], parfum[4] = nama_baru, int(harga_baru), tipe_aroma_baru, deskripsi_baru
#                             print("Parfum berhasil diubah!")
#                             ditemukan = True
#                             break
#                     if not ditemukan:
#                         print("Parfum tidak ditemukan.")

#                 elif pilihan_admin == "4":
#                     id_ = input("ID parfum yang ingin dihapus: ")
#                     id_ = int(id_)
#                     ditemukan = False
#                     for parfum in parfumes:
#                         if parfum[0] == id_:
#                             parfumes.remove(parfum)
#                             print("Parfum berhasil dihapus!")
#                             ditemukan = True
#                             break
#                     if not ditemukan:
#                         print("Parfum tidak ditemukan.")

#                 elif pilihan_admin == "5":
#                     break
#                 else:
#                     print("Pilihan tidak valid.")

#         elif jenis_pengguna == 'pengguna':
#             while True:
#                 os.system('cls')

#                 if parfumes:
#                     print("Daftar Parfum:")
#                     for parfum in parfumes:
#                         print(f"ID: {parfum[0]}, Nama: {parfum[1]}, Aroma: {parfum[3]}")
#                         print(f"Harga: {parfum[2]}, Deskripsi: {parfum[4]}")
#                 else:
#                     print("Belum ada data parfum.")

#                 print("Pilih aksi:")
#                 print("1. Lihat Deskripsi Parfum")
#                 print("2. Keluar")
#                 pilihan_user = input("> ")
#                 if pilihan_user == '1':
#                     id_ = input("ID parfum untuk deskripsi: ")
#                     id_ = int(id_)
#                     ditemukan = False
#                     for parfum in parfumes:
#                         if parfum[0] == id_:
#                             print(f"Deskripsi Parfum {parfum[1]}: {parfum[4]}")
#                             ditemukan = True
#                             break
#                     if not ditemukan:
#                         print("Parfum tidak ditemukan.")
                
#                 elif pilihan_user == "2":
#                     break
#                 else:
#                     print("Pilihan tidak valid.")

#     elif pilihan_awal == "2":
#         nama_pengguna = input("Nama pengguna baru: ")
#         kata_sandi = input("Kata sandi baru: ")

#         sudah_terdaftar = False
#         for data in pengguna:
#             if data[0] == nama_pengguna:
#                 sudah_terdaftar = True
#                 break

#         if sudah_terdaftar:
#             print("Nama pengguna sudah digunakan.")
#         else:
#             pengguna.append([nama_pengguna, kata_sandi, 'pengguna'])
#             print(f"Pengguna {nama_pengguna} berhasil didaftarkan!")

#     elif pilihan_awal == "3":
#         print("Terima kasih telah menggunakan sistem ini.")
#         break

import os
data_mahasiswa = ["Ifnu", "Adi", "Ucup", "Michael"]

def clear_screen():
    os.system('cls || clear')

clear_screen()

def tampilkan_mahasiswa():
    result = []
    for i in range(len(data_mahasiswa)):
        result.append(f"Data ke {i+1}: {data_mahasiswa[i]}")
    return result

def tambah_data():
    inputUser = input("Data yang mau ditambahkan : ")
    data_mahasiswa.append(inputUser)
    return f"{inputUser} telah ditambahkan"

def ubah_data():
    index = int(input("Masukkan index yang mau diedit: "))
    data_baru = input("Masukkan nama baru: ")
    data_mahasiswa[index-1] = data_baru
    return f"Data ke {index} berhasil diubah menjadi {data_baru}"

def hapus_data():
    index_user = int(input("Masukkan index yang ingin dihapus: "))
    del_user = data_mahasiswa.pop(index_user-1)
    return f"{del_user} telah dihapus"

def menu():
    print("""
    Menu
    Lihat Data  >> 1
    Tambah Data >> 2
    Edit Data   >> 3
    Hapus Data  >> 4
    Keluar      >> 5
    """)

while True:
    menu()
    pilih = input("Masukan Pilihan menu >> ")
    clear_screen()
    match(pilih):
        case "1":
            print("=== Lihat Data ===")
            mahasiswa = tampilkan_mahasiswa()
            for mhs in mahasiswa:
                print(mhs)
            input("Enter.....")
            clear_screen()
        case "2":
            pesan = tambah_data()
            print(pesan)
            input("Enter....")
            clear_screen()
        case "3":
            print("Menu ubah data")
            mahasiswa = tampilkan_mahasiswa()
            for mhs in mahasiswa:
                print(mhs)
            pesan = ubah_data()
            print(pesan)
            input("Enter.....")
            clear_screen()
        case "4":
            print("Menu Hapus Data")
            mahasiswa = tampilkan_mahasiswa()
            for mhs in mahasiswa:
                print(mhs)
            pesan = hapus_data()
            print(pesan)
            input("Enter......")
            clear_screen()
        case "5":
            print("Anda memilih menu keluar. Sampai jumpa!")
            exit()
        case _:
            print(f"Menu {pilih} tidak tersedia")
            input("Enter.....")
            clear_screen()
