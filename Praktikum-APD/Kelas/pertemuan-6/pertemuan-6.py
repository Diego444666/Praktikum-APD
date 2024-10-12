# data_mahasiswa= {
#     "nama" : "ucup",
#     "nim" : "059"
# }

# for value in data_mahasiswa.values():
#     print(data_mahasiswa)



# del data_mahasiswa["nim"]
# cache = data_mahasiswa.pop("nim")

# print("Jumlah Data = ", len(data_mahasiswa))

# data_mahasiswa.update({"alamat": "samarinda"})
# data_mahasiswa.update({"alamat": "tgr"})
# data_mahasiswa['alamat'] = "samarinda"
# data_mahasiswa['alamat'] = "tgr"


# print(data_mahasiswa("namaah"))

# print(data_mahasiswa["nama"])

# # for data in data_mahasiswa:
# #     print(data)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

data_mahasiswa= {
    "nama" : "ucup",
    "nim" : "059",
    "matkul" : ["APD", "kalkulus"],
    "dosen" : {
        "nama": "pak"
    }
}

print(data_mahasiswa["dosen"] ["nama"])
