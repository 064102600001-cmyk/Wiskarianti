def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

while True:
    print("\n--- Program Cek Jumlah Hari ---")
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if bulan < 1 or bulan > 12:
        print("Bulan tidak valid! Harap masukkan angka 1-12.")
    else:
        # Menentukan jumlah hari
        if bulan in [1, 3, 5, 7, 8, 10, 12]:
            hari = 31
        elif bulan in [4, 6, 9, 11]:
            hari = 30
        elif bulan == 2:
            hari = 29 if is_kabisat(tahun) else 28

        print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah: {hari} hari")

    # Opsi perulangan
    ulang = input("\nApakah ingin mencoba lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Program selesai. Terima kasih!")
        break