import math

# Menyimpan hasil perhitungan
hasil_perhitungan = []

# Fungsi untuk menghitung luas dan keliling lingkaran
def hitung_lingkaran():
    try:
        radius = float(input("Masukkan radius lingkaran: "))
        luas = math.pi * radius ** 2
        keliling = 2 * math.pi * radius
        hasil = f"Lingkaran - Radius: {radius}, Luas: {luas:.2f}, Keliling: {keliling:.2f}"
        hasil_perhitungan.append(hasil)
        print(f"Luas lingkaran: {luas:.2f}, Keliling lingkaran: {keliling:.2f}")
    except ValueError:
        print("Input tidak valid! Masukkan angka yang valid.")

# Fungsi untuk menghitung luas trapesium
def hitung_trapesium():
    try:
        alas_bawah = float(input("Masukkan panjang alas bawah trapesium: "))
        alas_atas = float(input("Masukkan panjang alas atas trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        luas = 0.5 * (alas_bawah + alas_atas) * tinggi
        hasil = f"Trapesium - Alas bawah: {alas_bawah}, Alas atas: {alas_atas}, Tinggi: {tinggi}, Luas: {luas:.2f}"
        hasil_perhitungan.append(hasil)
        print(f"Luas trapesium: {luas:.2f}")
    except ValueError:
        print("Input tidak valid! Masukkan angka yang valid.")

# Fungsi untuk mencetak data hasil perhitungan
def cetak_data():
    if not hasil_perhitungan:
        print("Belum ada data perhitungan.")
    else:
        print("\n--- Data Perhitungan ---")
        for index, data in enumerate(hasil_perhitungan, 1):
            print(f"{index}. {data}")
        
        # Menyimpan data ke dalam file .rw
        simpan = input("\nApakah Anda ingin menyimpan data ke file .rw? (y/n): ").lower()
        if simpan == 'y':
            with open('data_perhitungan.rx', 'w') as file:
                for data in hasil_perhitungan:
                    file.write(data + '\n')
            print("Data berhasil disimpan ke 'data_perhitungan.rt'.")

# Fungsi untuk menampilkan menu utama
def tampilkan_menu():
    print("\n--- Menu Utama ---")
    print("1. Hitung luas Lingkaran")
    print("2. Hitung luas Trapesium")
    print("3. Cetak Data")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")
    return pilihan

# Fungsi utama program
def main():
    while True:
        pilihan = tampilkan_menu()

        if pilihan == "1":
            hitung_lingkaran()
        elif pilihan == "2":
            hitung_trapesium()
        elif pilihan == "3":
            cetak_data()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan pilih lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
