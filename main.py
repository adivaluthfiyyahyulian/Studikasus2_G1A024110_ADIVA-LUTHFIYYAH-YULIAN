import csv
import os
import time
import math
from multiprocessing import Pool, cpu_count
from collections import Counter

DATA_FILE = "data_cuaca_lokal.csv"
OUTPUT_FILE = "hasil_analisis_cuaca.csv"


def hitung_risiko(row):
    """Menghitung skor risiko cuaca sederhana dari data simulasi."""
    hujan = float(row["curah_hujan_mm"])
    angin = float(row["kecepatan_angin_kmh"])
    suhu = float(row["suhu_c"])

    skor = 0
    if hujan >= 100:
        skor += 3
    elif hujan >= 50:
        skor += 2
    elif hujan >= 25:
        skor += 1

    if angin >= 60:
        skor += 2
    elif angin >= 35:
        skor += 1

    if suhu >= 35 or suhu <= 18:
        skor += 1

    if skor >= 5:
        kategori = "Tinggi"
    elif skor >= 3:
        kategori = "Sedang"
    else:
        kategori = "Rendah"

    return {
        "wilayah": row["wilayah"],
        "curah_hujan_mm": hujan,
        "kecepatan_angin_kmh": angin,
        "suhu_c": suhu,
        "skor_risiko": skor,
        "kategori_risiko": kategori,
    }


def beban_komputasi(row):
    """Fungsi kerja tambahan untuk mensimulasikan perhitungan berulang."""
    hasil = hitung_risiko(row)
    angka = float(row["curah_hujan_mm"]) + float(row["kecepatan_angin_kmh"])
    nilai = 0.0
    for i in range(500):
        nilai += math.sqrt(angka + i + 1)
    hasil["nilai_simulasi"] = round(nilai, 3)
    return hasil


def baca_data():
    with open(DATA_FILE, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def simpan_hasil(data):
    kolom = [
        "wilayah", "curah_hujan_mm", "kecepatan_angin_kmh",
        "suhu_c", "skor_risiko", "kategori_risiko", "nilai_simulasi"
    ]
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=kolom)
        writer.writeheader()
        writer.writerows(data)


def tampilkan_ringkasan(hasil, durasi_serial, durasi_paralel):
    jumlah = Counter(item["kategori_risiko"] for item in hasil)
    print("\n=== HASIL ANALISIS RISIKO CUACA ===")
    print(f"Jumlah data dianalisis : {len(hasil)}")
    print(f"Risiko tinggi          : {jumlah.get('Tinggi', 0)} wilayah/data")
    print(f"Risiko sedang          : {jumlah.get('Sedang', 0)} wilayah/data")
    print(f"Risiko rendah          : {jumlah.get('Rendah', 0)} wilayah/data")
    print(f"\nWaktu serial            : {durasi_serial:.4f} detik")
    print(f"Waktu paralel           : {durasi_paralel:.4f} detik")

    if durasi_paralel > 0:
        print(f"Perbandingan kecepatan  : {durasi_serial / durasi_paralel:.2f}x")
    print(f"\nFile hasil disimpan ke  : {OUTPUT_FILE}")
    print("\nCatatan: kategori ini adalah contoh pembelajaran, bukan peringatan resmi cuaca.")


def main():
    if not os.path.exists(DATA_FILE):
        print(f"File {DATA_FILE} tidak ditemukan. Letakkan file CSV di folder yang sama.")
        return

    data = baca_data()
    if not data:
        print("Dataset kosong.")
        return

    # Pemrosesan serial: satu per satu pada satu proses.
    mulai = time.perf_counter()
    hasil_serial = [beban_komputasi(row) for row in data]
    durasi_serial = time.perf_counter() - mulai

    # Pemrosesan paralel: pekerjaan dibagi ke beberapa proses CPU.
    jumlah_proses = max(1, min(cpu_count(), 4))
    mulai = time.perf_counter()
    with Pool(processes=jumlah_proses) as pool:
        hasil_paralel = pool.map(beban_komputasi, data)
    durasi_paralel = time.perf_counter() - mulai

    # Simpan hasil paralel; hasil analisis sama, cara pemrosesannya berbeda.
    simpan_hasil(hasil_paralel)
    print(f"Proses CPU yang digunakan: {jumlah_proses}")
    tampilkan_ringkasan(hasil_paralel, durasi_serial, durasi_paralel)


if __name__ == "__main__":
    main()
