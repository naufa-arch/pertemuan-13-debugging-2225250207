
def baca_nilai(nama_file):
    nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    angka = float(teks_nilai)
                    nilai.append(angka)
                    print(f"{nim}: {angka}")
                except ValueError:
                    print(f"Data tidak valid: {baris}")

    except FileNotFoundError:
        print("File nilai tidak ditemukan.")
        return []

    return nilai


data_nilai = baca_nilai("data/nilai.txt")

if data_nilai:
    rata_rata = sum(data_nilai) / len(data_nilai)
    print(f"Rata-rata nilai valid: {rata_rata:.2f}")
else:
    print("Tidak ada nilai valid.")
