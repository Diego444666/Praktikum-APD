import os

pengguna = [
    ["fachlevi muhammad", "059", "admin"],
]

parfumes = [
    [1, "HMNS Essence", 300000, "Woody", "HMNS Essence memberikan aroma yang  dan strong dengan sentuhan kayu yang elegan."],
    [2, "HMNS Orgasm", 450000, "Floral", "HMNS Orgasm memiliki aroma floral yang segar dan flirty, cocok untuk momen tender."]
]
os.system('cls')

print("Selamat datang diParfume by HMNS")
while True:
    print("Silakan pilih aksi:")
    print("1. Masuk")
    print("2. Daftar")
    print("3. Keluar")
    pilihan_awal = input("> ")

    if pilihan_awal == '1':
        for percobaan in range(3):
            nama_pengguna = input("Nama pengguna: ")
            kata_sandi = input("Kata sandi: ")
            jenis_pengguna = None
            for data in pengguna:
                if data[0] == nama_pengguna and data[1] == kata_sandi:
                    print(f"Selamat datang, {nama_pengguna}!")
                    jenis_pengguna = data[2]
                    break
            if jenis_pengguna:
                break
            else:
                print(f"Nama pangguna atau kata sandi salah. Kesempatan tersisa: {2 - percobaan}")

        if not jenis_pengguna:
            print("Gagal masuk setelah 3 kali percobaan.")
            continue

        if jenis_pengguna == 'admin':
            while True:
                os.system('cls')
                if parfumes:
                    print("Daftar Parfum:")
                    for parfum in parfumes:
                        print(f"ID: {parfum[0]}, Nama: {parfum[1]}, Aroma: {parfum[3]}")
                        print(f"Harga: {parfum[2]}, Deskripsi: {parfum[4]}")
                else:
                    print("Belum ada data parfume.")

                print("Pilih aksi:")
                print("1. Tambah Parfum")
                print("2. Lihat Deskripsi Parfum")
                print("3. Ubah Parfum")
                print("4. Hapus Parfum")
                print("5. Keluar")
                pilihan_admin = input("> ")

                if pilihan_admin == "1":
                    id_ = input("ID: ")
                    nama = input("Nama parfum: ")
                    harga = input("Harga: ")
                    tipe_aroma = input("Tipe aroma: ")
                    deskripsi = input("Deskripsi: ")
                    parfumes.append([int(id_), nama, int(harga), tipe_aroma, deskripsi])
                    print(f"Parfum {nama} berhasil ditambahkan!")

                elif pilihan_admin == "2":
                    id_ = input("ID parfum untuk deskripsi: ")
                    id_ = int(id_)
                    ditemukan = False
                    for parfum in parfumes:
                        if parfum[0] == id_:
                            print(f"Deskripsi Parfum {parfum[1]}: {parfum[4]}")
                            ditemukan = True
                            break
                    if not ditemukan:
                        print("Parfum tidak ditemukan.")

                elif pilihan_admin == "3":
                    id_ = input("ID parfum yang ingin diubah: ")
                    id_ = int(id_)
                    ditemukan = False
                    for parfum in parfumes:
                        if parfum[0] == id_:
                            nama_baru = input("Nama baru: ")
                            harga_baru = input("Harga baru: ")
                            tipe_aroma_baru = input("Tipe aroma baru: ")
                            deskripsi_baru = input("Deskripsi baru: ")
                            parfum[1], parfum[2], parfum[3], parfum[4] = nama_baru, int(harga_baru), tipe_aroma_baru, deskripsi_baru
                            print("Parfum berhasil diubah!")
                            ditemukan = True
                            break
                    if not ditemukan:
                        print("Parfum tidak ditemukan.")

                elif pilihan_admin == "4":
                    id_ = input("ID parfum yang ingin dihapus: ")
                    id_ = int(id_)
                    ditemukan = False
                    for parfum in parfumes:
                        if parfum[0] == id_:
                            parfumes.remove(parfum)
                            print("Parfum berhasil dihapus!")
                            ditemukan = True
                            break
                    if not ditemukan:
                        print("Parfum tidak ditemukan.")

                elif pilihan_admin == "5":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif jenis_pengguna == 'pengguna':
            while True:
                os.system('cls')

                if parfumes:
                    print("Daftar Parfum:")
                    for parfum in parfumes:
                        print(f"ID: {parfum[0]}, Nama: {parfum[1]}, Aroma: {parfum[3]}")
                        print(f"Harga: {parfum[2]}, Deskripsi: {parfum[4]}")
                else:
                    print("Belum ada data parfum.")

                print("Pilih aksi:")
                print("1. Lihat Deskripsi Parfum")
                print("2. Keluar")
                pilihan_user = input("> ")
                if pilihan_user == '1':
                    id_ = input("ID parfum untuk deskripsi: ")
                    id_ = int(id_)
                    ditemukan = False
                    for parfum in parfumes:
                        if parfum[0] == id_:
                            print(f"Deskripsi Parfum {parfum[1]}: {parfum[4]}")
                            ditemukan = True
                            break
                    if not ditemukan:
                        print("Parfum tidak ditemukan.")
                
                elif pilihan_user == "2":
                    break
                else:
                    print("Pilihan tidak valid.")

    elif pilihan_awal == "2":
        nama_pengguna = input("Nama pengguna baru: ")
        kata_sandi = input("Kata sandi baru: ")

        sudah_terdaftar = False
        for data in pengguna:
            if data[0] == nama_pengguna:
                sudah_terdaftar = True
                break

        if sudah_terdaftar:
            print("Nama pengguna sudah digunakan.")
        else:
            pengguna.append([nama_pengguna, kata_sandi, 'pengguna'])
            print(f"Pengguna {nama_pengguna} berhasil didaftarkan!")

    elif pilihan_awal == "3":
        print("Terima kasih telah menggunakan sistem ini.")
        break

