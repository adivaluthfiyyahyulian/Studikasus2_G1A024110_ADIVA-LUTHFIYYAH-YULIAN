# Studi Kasus HPC: Analisis Risiko Cuaca Lokal dengan Komputasi Paralel

## 1. Latar Belakang
High-Performance Computing (HPC) membantu menyelesaikan perhitungan besar dengan membagi pekerjaan ke beberapa sumber daya komputasi. Studi kasus ini menerapkan gagasan tersebut pada analisis data cuaca lokal, yang dapat membantu peneliti memahami data curah hujan, kecepatan angin, dan suhu.

## 2. Tujuan
- Mengolah dataset cuaca simulasi.
- Mengelompokkan data berdasarkan skor risiko sederhana.
- Membandingkan pemrosesan serial dan paralel menggunakan Python.
- Menunjukkan bagaimana komputasi paralel dapat menjadi dasar untuk analisis data berskala lebih besar.

## 3. Data yang Digunakan
File `data_cuaca_lokal.csv` berisi 3.000 baris data simulasi dengan kolom wilayah, curah hujan, kecepatan angin, dan suhu. Data ini dibuat untuk pembelajaran, bukan data cuaca resmi.

## 4. Metode
1. Membaca data CSV.
2. Menghitung skor risiko sederhana berdasarkan curah hujan, kecepatan angin, dan suhu.
3. Memproses data secara serial (satu per satu).
4. Memproses data secara paralel menggunakan `multiprocessing.Pool`.
5. Membandingkan waktu proses dan menyimpan hasil analisis ke `hasil_analisis_cuaca.csv`.

Kategori risiko dalam proyek ini hanya contoh aturan sederhana untuk demonstrasi coding, bukan standar meteorologi atau peringatan resmi.

## 5. Teknologi
- Python 3
- `csv`, `time`, `math`, `multiprocessing`, dan `collections` (modul bawaan Python)

## 6. Cara Menjalankan
Jalankan dari terminal di folder proyek:

```bash
python main.py
```

Program akan menampilkan ringkasan kategori risiko dan waktu pemrosesan serial/paralel. Hasil lengkap tersimpan di `hasil_analisis_cuaca.csv`.

## 7. Hasil yang Diharapkan
Program menampilkan jumlah data dalam kategori risiko rendah, sedang, dan tinggi, serta perbandingan waktu serial dan paralel. Waktu aktual bergantung pada spesifikasi komputer; pemrosesan paralel tidak selalu lebih cepat untuk setiap ukuran data karena ada biaya pembentukan proses dan pembagian pekerjaan.

## 8. Kesimpulan
Proyek ini memperagakan prinsip dasar komputasi paralel yang berkaitan dengan HPC. Untuk penelitian nyata, analisis perlu menggunakan data cuaca tepercaya, validasi metode risiko oleh ahli, dan infrastruktur komputasi yang sesuai. Menjalankan program ini di komputer biasa bukan berarti menggunakan superkomputer atau layanan HPC sungguhan.
