import os
import socket
import subprocess
from datetime import datetime

ROUTER = "192.168.1.1"  # ganti dengan Default Gateway dari ipconfig
DNS_SERVER = "8.8.8.8"
DOMAIN = "google.com"
FOLDER_LAPORAN = "laporan"


def ping(alamat):
    hasil = subprocess.run(
        ["ping", "-n", "2", "-w", "1500", alamat],
        capture_output=True,
        text=True,
    )
    return hasil.returncode == 0 and "TTL=" in hasil.stdout


def cek_dns(domain):
    try:
        return True, socket.gethostbyname(domain)
    except socket.gaierror:
        return False, None


def diagnosa(router_ok, internet_ok, dns_ok):
    if not router_ok:
        return "Masalah di jaringan lokal: cek kabel/WiFi, router, atau adapter jaringan."
    if not internet_ok:
        return "Router terjangkau tetapi internet putus: cek modem atau hubungi penyedia internet (ISP)."
    if not dns_ok:
        return "Internet jalan tetapi nama domain gagal dikenali: kemungkinan masalah DNS."
    return "Semua normal."


def status(ok):
    return "OK" if ok else "GAGAL"


def main():
    waktu = datetime.now()
    router_ok = ping(ROUTER)
    internet_ok = ping(DNS_SERVER)
    dns_ok, ip = cek_dns(DOMAIN)

    baris = [
        "LAPORAN CEK JARINGAN",
        f"Waktu     : {waktu.strftime('%Y-%m-%d %H:%M:%S')}",
        "-" * 50,
        f"Router ({ROUTER}) : {status(router_ok)}",
        f"Internet ({DNS_SERVER}) : {status(internet_ok)}",
        f"DNS ({DOMAIN}) : {status(dns_ok)}" + (f" -> {ip}" if ip else ""),
        "-" * 50,
        "Diagnosa  : " + diagnosa(router_ok, internet_ok, dns_ok),
    ]

    for b in baris:
        print(b)

    os.makedirs(FOLDER_LAPORAN, exist_ok=True)
    nama_file = f"laporan_{waktu.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(os.path.join(FOLDER_LAPORAN, nama_file), "w", encoding="utf-8") as f:
        f.write("\n".join(baris))
    print(f"\nLaporan disimpan: {FOLDER_LAPORAN}\\{nama_file}")


if __name__ == "__main__":
    main()