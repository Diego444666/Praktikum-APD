def biodata():
  nama = input("Masukkan nama kamu: ")
  umur = int(input("Masukkan umur kamu: "))
  tb = float(input("Masukkan tinggi badan kamu (dalam cm): "))
  mahasiswa = bool(int(input("Apakah kamu seorang mahasiswa? (1=Ya, 0=Tidak): ")))
  total = umur + tb

  print("--------------------------------")
  print("           Bio Data Anda")
  print("--------------------------------")
  print("Nama            :", nama)
  print("Umur            :", umur, "tahun")
  print("Tinggi Badan    :", tb, "cm")
  print("Mahasiswa       :", mahasiswa)
  print("Total Angka     :", total)
  print("--------------------------------")
biodata()