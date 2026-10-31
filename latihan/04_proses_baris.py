with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if not baris:
            continue

        nim, teks_nilai = baris.split(",")
        nilai = float(teks_nilai)

        print("NIM:", nim)
        print("Nilai:", nilai)
        print("----------------")