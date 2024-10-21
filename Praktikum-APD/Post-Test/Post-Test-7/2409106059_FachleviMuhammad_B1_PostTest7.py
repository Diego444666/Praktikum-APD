import os
import time

def loading():
    for i in range(1, 4):
        print(f"Loading {i}...", end="\r")
        time.sleep(1)

pengguna = {"fachlevi muhammad": {"password": "059", "role": "admin"}}
parfumes = {
    1: {"nama": "HMNS Essence", "harga": 300000, "aroma": "Woody", "deskripsi": "Aroma strong dengan sentuhan kayu elegan."},
    2: {"nama": "HMNS Orgasm", "harga": 450000, "aroma": "Floral", "deskripsi": "Aroma floral yang segar dan flirty."}
}

def menu_utama():
    while True:
        os.system('cls')
        print("Selamat datang di Parfume by HMNS")
        print("\nPilih aksi:")
        print("1. Masuk")
        print("2. Daftar")
        print("3. Keluar")
        pilihan = input("> ")

        if pilihan == "1":  
            role = login()
            if role == "admin":
                menu_admin()
            elif role == "pengguna":
                menu_pengguna()
        elif pilihan == "2":
            daftar_pengguna()
        elif pilihan == "3":
            loading()
            print("Terima kasih telah menggunakan sistem ini.")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak valid.")
            time.sleep(1)

def login(attempts=3):
    if attempts == 0:
        print("Gagal masuk setelah 3 kali percobaan.")
        return None
    
    nama_pengguna = input("Nama pengguna: ")
    kata_sandi = input("Kata sandi: ")
    user = pengguna.get(nama_pengguna)
    
    if user and user["password"] == kata_sandi:
        print(f"Selamat datang, {nama_pengguna}!")
        loading()
        return user["role"]
    else:
        print(f"Nama pengguna atau kata sandi salah. Coba lagi.")
        time.sleep(1)
        return login(attempts - 1)

def daftar_pengguna():
    nama_pengguna = input("Nama pengguna baru: ")
    kata_sandi = input("Kata sandi baru: ")
    if nama_pengguna in pengguna:
        print("Nama pengguna sudah digunakan.")
    else:
        pengguna[nama_pengguna] = {"password": kata_sandi, "role": "pengguna"}
        print(f"Pengguna {nama_pengguna} berhasil didaftarkan!")
    loading()
    time.sleep(1)

def menu_admin():
    while True:
        os.system('cls')
        tampilkan_parfum()
        print("\nPilih aksi:")
        print("1. Tambah Parfum")
        print("2. Lihat Deskripsi Parfum")
        print("3. Ubah Parfum")
        print("4. Hapus Parfum")
        print("5. Keluar")
        pilihan = input("> ")

        if pilihan == "1":
            tambah_parfum()
        elif pilihan == "2":
            lihat_deskripsi()
        elif pilihan == "3":
            ubah_parfum()
        elif pilihan == "4":
            hapus_parfum()
        elif pilihan == "5":
            loading()
            break
        else:
            print("Pilihan tidak valid.")
        time.sleep(1)

def menu_pengguna():
    while True:
        os.system('cls')
        tampilkan_parfum()
        print("\nPilih aksi:")
        print("1. Lihat Deskripsi Parfum")
        print("2. Keluar")
        pilihan = input("> ")

        if pilihan == "1":
            lihat_deskripsi()
        elif pilihan == "2":
            loading()
            break
        else:
            print("Pilihan tidak valid.")
        time.sleep(1)

def tambah_parfum():
    try:
        id_ = int(input("ID: "))
        if id_ in parfumes:
            print("ID sudah digunakan, silakan gunakan ID lain.")
            return
        nama = input("Nama parfum: ")
        harga = int(input("Harga: "))
        aroma = input("Aroma: ")
        deskripsi = input("Deskripsi: ")
        parfumes[id_] = {"nama": nama, "harga": harga, "aroma": aroma, "deskripsi": deskripsi}
        print(f"Parfum {nama} berhasil ditambahkan!")
        loading()
    except ValueError:
        print("Input salah, ID dan harga harus angka.")

def lihat_deskripsi():
    try:
        id_ = int(input("ID parfum: "))
        parfum = parfumes.get(id_)
        if parfum:
            print(f"Deskripsi Parfum {parfum['nama']}: {parfum['deskripsi']}")
        else:
            print("Parfum tidak ditemukan.")
    except ValueError:
        print("ID harus berupa angka.")

def ubah_parfum():
    try:
        id_ = int(input("ID parfum yang ingin diubah: "))
        if id_ in parfumes:
            nama_baru = input("Nama baru: ")
            harga_baru = int(input("Harga baru: "))
            aroma_baru = input("Aroma baru: ")
            deskripsi_baru = input("Deskripsi baru: ")
            parfumes[id_].update({"nama": nama_baru, "harga": harga_baru, "aroma": aroma_baru, "deskripsi": deskripsi_baru})
            print("Parfum berhasil diubah!")
            loading()
        else:
            print("Parfum tidak ditemukan.")
    except ValueError:
        print("ID dan harga harus berupa angka.")

def hapus_parfum():
    try:
        id_ = int(input("ID parfum yang ingin dihapus: "))
        if id_ in parfumes:
            del parfumes[id_]
            print("Parfum berhasil dihapus!")
            loading()
        else:
            print("Parfum tidak ditemukan.")
    except ValueError:
        print("ID harus berupa angka.")

def tampilkan_parfum():
    if parfumes:
        for id_, parfum in parfumes.items():
            print(f"ID: {id_}, Nama: {parfum['nama']}, Aroma: {parfum['aroma']}, Harga: {parfum['harga']}")
    else:
        print("Belum ada data parfum.")

menu_utama()
