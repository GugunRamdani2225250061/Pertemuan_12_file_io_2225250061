def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Melewati baris kosong
                if not baris:
                    continue

                try:
                    # Memisahkan NIM dan nilai
                    nim, teks_nilai = baris.split(",")

                    # Mengubah nilai menjadi float
                    nilai = float(teks_nilai)

                    # Menyimpan data yang valid
                    data.append((nim.strip(), nilai))

                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    # Mengambil seluruh nilai
    nilai = [item[1] for item in data]

    # Menghitung statistik
    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    nilai_minimum = min(nilai)
    nilai_maksimum = max(nilai)

    # Menghitung jumlah mahasiswa yang lulus
    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    # Menulis hasil rekap ke file
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("HASIL REKAP NILAI MAHASISWA\n")
        file.write("===========================\n")
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_minimum:.2f}\n")
        file.write(f"Maksimum: {nilai_maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

    print("\nRekap nilai berhasil dibuat.")


# Program utama
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

# Membaca dan memvalidasi data
data_mahasiswa = baca_data(input_file)

# Menulis hasil rekap
tulis_rekap(output_file, data_mahasiswa)

# Menampilkan ringkasan pada terminal
if data_mahasiswa:
    nilai = [item[1] for item in data_mahasiswa]

    print("\nRINGKASAN NILAI MAHASISWA")
    print("=========================")
    print("Jumlah data valid:", len(nilai))
    print(f"Rata-rata: {sum(nilai) / len(nilai):.2f}")
    print(f"Nilai minimum: {min(nilai):.2f}")
    print(f"Nilai maksimum: {max(nilai):.2f}")
    print("Jumlah lulus:", sum(1 for x in nilai if x >= 60))