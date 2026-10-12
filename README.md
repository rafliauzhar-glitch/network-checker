# Network Checker

Script Python sederhana untuk mengecek koneksi jaringan dan memberi diagnosa awal letak masalahnya. Dibuat sebagai latihan troubleshooting jaringan dasar untuk IT Support.

## Fitur

- Ping ke router (mengecek jaringan lokal)
- Ping ke internet (`8.8.8.8`)
- Cek DNS (menerjemahkan nama domain menjadi alamat IP)
- Diagnosa otomatis dari hasil ketiga tes
- Laporan dengan waktu pengecekan disimpan ke file `.txt` di folder `laporan/`

## Cara Membaca Diagnosa

| Router | Internet | DNS | Kesimpulan |
|---|---|---|---|
| GAGAL | - | - | Masalah di jaringan lokal (kabel, WiFi, router, adapter) |
| OK | GAGAL | - | Router terjangkau tetapi internet putus (modem atau ISP) |
| OK | OK | GAGAL | Internet jalan tetapi nama domain gagal dikenali (masalah DNS) |
| OK | OK | OK | Semua normal |

## Cara Menjalankan

1. Clone repo ini, lalu masuk ke foldernya.
2. Cari alamat router dengan perintah `ipconfig`, lalu lihat **Default Gateway**.
3. Buka `network_checker.py` dan ubah baris `ROUTER = "192.168.1.1"` sesuai Default Gateway tersebut.
4. Jalankan:
```
   python network_checker.py
```

Tidak perlu memasang library tambahan. Script hanya memakai modul bawaan Python dan perintah `ping` bawaan Windows.

## Contoh Hasil

```
LAPORAN CEK JARINGAN
Waktu     : 2026-10-13 06:43:34
--------------------------------------------------
Router (192.168.1.1) : OK
Internet (8.8.8.8) : OK
DNS (google.com) : OK -> 74.125.24.100
--------------------------------------------------
Diagnosa  : Semua normal.
```

## Rencana Pengembangan

- Mengecek beberapa perangkat sekaligus (printer, server)
- Menjalankan pengecekan berulang setiap beberapa menit
- Menampilkan hasil `tracert` saat internet gagal