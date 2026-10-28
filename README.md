# Pertemuan 13 - Debugging dan Testing

**Nama:** Hashifah Naufa Setiawan  
**NIM:** 2225250207 
**Kelas:** 3E

## Kasus

Program yang diuji adalah program Python untuk menghitung rata-rata nilai mahasiswa, menentukan status kelulusan, dan mencari nilai tertinggi. Pengujian dilakukan untuk menemukan kesalahan pada kode, memperbaiki logika program, dan memastikan hasilnya sesuai dengan yang diharapkan.

## Test Case

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| TC01 | `[80, 60, 90, 70]` untuk rata-rata | 75.0 | 60.0 karena pembagi ditetapkan 5 | Gagal |
| TC02 | Nilai `60` untuk status | Tidak lulus jika syaratnya `nilai > 60` | Tidak lulus | Berhasil |
| TC03 | `[80, 60, 90, 70]` untuk nilai tertinggi | 90 | 0 karena kondisi perbandingan terbalik | Gagal |
| TC04 | `[80, 60, 90, 70]` setelah perbaikan | Rata-rata 75.0 dan nilai tertinggi 90 | Sesuai hasil yang diharapkan | Berhasil |

## Bug Report

**1. Bug pada fungsi rata-rata**

- **Gejala:** Hasil rata-rata tidak sesuai dengan data.
- **Lokasi:** Fungsi `hitung_rata_rata()`.
- **Akar penyebab:** Program membagi jumlah nilai dengan angka tetap `5`, padahal jumlah data yang diuji adalah `4`.
- **Perbaikan:** Mengganti pembagi `5` dengan `len(nilai)` agar jumlah data dihitung secara otomatis.

**2. Bug pada fungsi nilai tertinggi**

- **Gejala:** Program menghasilkan nilai tertinggi yang salah.
- **Lokasi:** Kondisi percabangan di dalam fungsi `nilai_tertinggi()`.
- **Akar penyebab:** Kondisi `x < tertinggi` digunakan untuk mencari nilai yang lebih kecil, bukan nilai yang lebih besar.
- **Perbaikan:** Mengubah kondisi menjadi `x > tertinggi` dan menginisialisasi `tertinggi` menggunakan `nilai[0]`.

## Retest

Setelah perbaikan, program dijalankan kembali dengan data `[80, 60, 90, 70]`.

| Pengujian | Hasil Setelah Perbaikan | Status |
|---|---|---|
| Menghitung rata-rata | 75.0 | Berhasil |
| Menentukan status nilai 60 | Tidak lulus | Berhasil |
| Mencari nilai tertinggi | 90 | Berhasil |

Hasil pengujian menunjukkan bahwa fungsi rata-rata dan nilai tertinggi sudah bekerja sesuai harapan. Fungsi status juga berjalan sesuai aturan `nilai > 60`.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek:

```bash
python3 praktik/praktik_4_debugging.py
```

Jika perintah `python3` tidak berfungsi di Windows, gunakan:

```bash
python praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah menjalankan program secara bertahap dan memeriksa nilai variabel untuk mengetahui letak kesalahan. Dengan teknik ini, saya dapat menemukan kesalahan pada pembagi rata-rata dan kondisi perbandingan dalam fungsi nilai tertinggi. Saya belajar bahwa program yang dapat dijalankan belum tentu menghasilkan jawaban yang benar, sehingga pengujian menggunakan beberapa test case sangat penting untuk memastikan logika program sesuai dengan tujuan.