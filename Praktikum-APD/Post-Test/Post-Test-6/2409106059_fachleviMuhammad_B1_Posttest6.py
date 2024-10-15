import os
import time

pengguna = {
    "fachlevi muhammad": {"password": "059", "role": "admin"},
}

parfumes = {
    1: {"nama": "HMNS Essence", "harga": 300000, "aroma": "Woody", "deskripsi": "HMNS Essence memberikan aroma yang dan strong dengan sentuhan kayu yang elegan."},
    2: {"nama": "HMNS Orgasm", "harga": 450000, "aroma": "Floral", "deskripsi": "HMNS Orgasm memiliki aroma floral yang segar dan flirty, cocok untuk momen tender."}
}

os.system('cls')
print("Selamat datang di Parfume by HMNS")

while True:
    print("\nSilakan pilih aksi:")
    print("1. Masuk")
    print("2. Daftar")
    print("3. Keluar")
    pilihan_awal = input("> ")

    if pilihan_awal == '1':
        for percobaan in range(3):
            nama_pengguna = input("Nama pengguna: ")
            kata_sandi = input("Kata sandi: ")
            user = pengguna.get(nama_pengguna)

            if user and user["password"] == kata_sandi:
                print(f"Selamat datang, {nama_pengguna}!")
                jenis_pengguna = user["role"]
                for i in range(1, 4):
                    print(f"Loading {i}...")
                    time.sleep(1)
                break
            else:
                print(f"Nama pengguna atau kata sandi salah. Kesempatan tersisa: {2 - percobaan}")
                time.sleep(1)

        if not user:
            print("Gagal masuk setelah 3 kali percobaan.")
            continue

        if jenis_pengguna == 'admin':
            while True:
                os.system('cls')
                if parfumes:
                    print("Daftar Parfum:")
                    for id_, parfum in parfumes.items():
                        print(f"ID: {id_}, Nama: {parfum['nama']}, Aroma: {parfum['aroma']}")
                        print(f"Harga: {parfum['harga']}, Deskripsi: {parfum['deskripsi']}")
                else:
                    print("Belum ada data parfum.")

                print("\nPilih aksi:")
                print("1. Tambah Parfum")
                print("2. Lihat Deskripsi Parfum")
                print("3. Ubah Parfum")
                print("4. Hapus Parfum")
                print("5. Keluar")
                pilihan_admin = input("> ")

                if pilihan_admin == "1":
                    id_ = int(input("ID: "))
                    nama = input("Nama parfum: ")
                    harga = int(input("Harga: "))
                    tipe_aroma = input("Tipe aroma: ")
                    deskripsi = input("Deskripsi: ")
                    parfumes[id_] = {"nama": nama, "harga": harga, "aroma": tipe_aroma, "deskripsi": deskripsi}
                    print(f"Parfum {nama} berhasil ditambahkan!")
                    for i in range(1, 4):
                        print(f"Loading {i}...")
                        time.sleep(1)

                elif pilihan_admin == "2":
                    id_ = int(input("ID parfum untuk deskripsi: "))
                    parfum = parfumes.get(id_)
                    if parfum:
                        print(f"Deskripsi Parfum {parfum['nama']}: {parfum['deskripsi']}")
                    else:
                        print("Parfum tidak ditemukan.")
                    for i in range(1, 4):
                        print(f"Loading {i}...")
                        time.sleep(1)

                elif pilihan_admin == "3":
                    id_ = int(input("ID parfum yang ingin diubah: "))
                    parfum = parfumes.get(id_)
                    if parfum:
                        nama_baru = input("Nama baru: ")
                        harga_baru = int(input("Harga baru: "))
                        tipe_aroma_baru = input("Tipe aroma baru: ")
                        deskripsi_baru = input("Deskripsi baru: ")
                        parfumes[id_].update({"nama": nama_baru, "harga": harga_baru, "aroma": tipe_aroma_baru, "deskripsi": deskripsi_baru})
                        print("Parfum berhasil diubah!")
                    else:
                        print("Parfum tidak ditemukan.")
                    for i in range(1, 4):
                        print(f"Loading {i}...")
                        time.sleep(1)

                elif pilihan_admin == "4":
                    id_ = int(input("ID parfum yang ingin dihapus: "))
                    if id_ in parfumes:
                        del parfumes[id_]
                        print("Parfum berhasil dihapus!")
                    else:
                        print("Parfum tidak ditemukan.")
                    for i in range(1, 4):
                        print(f"Loading {i}...")
                        time.sleep(1)

                elif pilihan_admin == "5":
                    for i in range(1, 4):
                        print(f"Loading {i}...")
                        time.sleep(1)
                    break
                else:
                    print("Pilihan tidak valid.")
                    time.sleep(1)

        elif jenis_pengguna == 'pengguna':
            while True:
                os.system('cls')
                if parfumes:
                    print("Daftar Parfum:")
                    for id_, parfum in parfumes.items():
                        print(f"ID: {id_}, Nama: {parfum['nama']}, Aroma: {parfum['aroma']}")
                        print(f"Harga: {parfum['harga']}, Deskripsi: {parfum['deskripsi']}")
                else:
                    print("Belum ada data parfum.")

                print("\nPilih aksi:")
                print("1. Lihat Deskripsi Parfum")
                print("2. Keluar")
                pilihan_user = input("> ")

                if pilihan_user == '1':
                    id_ = int(input("ID parfum untuk deskripsi: "))
                    parfum = parfumes.get(id_)
                    if parfum:
                        print(f"Deskripsi Parfum {parfum['nama']}: {parfum['deskripsi']}")
                    else:
                        print("Parfum tidak ditemukan.")
                    
                    for i in range(1, 4):
                        print(f"Loading {i}...")
                        time.sleep(1)

                elif pilihan_user == "2":
                    for i in range(1, 4):
                        print(f"Loading {i}...")
                        time.sleep(1)
                    break
                else:
                    print("Pilihan tidak valid.")
                    time.sleep(1)

    elif pilihan_awal == "2":
        nama_pengguna = input("Nama pengguna baru: ")
        kata_sandi = input("Kata sandi baru: ")

        if nama_pengguna in pengguna:
            print("Nama pengguna sudah digunakan.")
        else:
            pengguna[nama_pengguna] = {"password": kata_sandi, "role": "pengguna"}
            print(f"Pengguna {nama_pengguna} berhasil didaftarkan!")

        for i in range(1, 4):
            print(f"Loading {i}...")
            time.sleep(1)

    elif pilihan_awal == "3":
        print("Terima kasih telah menggunakan sistem ini.")
        for i in range(1, 4):
            print(f"Loading {i}...")
            time.sleep(1)
        break
    else:
        print("Pilihan tidak valid.")
        time.sleep(1)

