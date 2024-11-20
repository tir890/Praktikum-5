data_mahasiswa = {}

def hitung_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tampilkan():
    print("\nDaftar Nilai")
    print("=" * 63)
    print("| NO |    NIM    |   NAMA   | TUGAS |  UTS  |  UAS  |  AKHIR  |")
    print("=" * 63)
    if data_mahasiswa:
        for i, (nim, mhs) in enumerate(data_mahasiswa.items(), start=1):
            print(f"| {i:2} | {nim:8} | {mhs['nama']:<8} | {mhs['tugas']:5.1f} | {mhs['uts']:5.1f} | {mhs['uas']:5.1f} | {mhs['akhir']:7.2f} |")
    else:
        print("|                          TIDAK ADA DATA                          |")
    print("=" * 63)

def tambah_ubah(nim=None):
    nim = nim or input("NIM: ")
    nama = input("Nama: ")
    tugas, uts, uas = [float(input(f"Nilai {x}: ")) for x in ["Tugas", "UTS", "UAS"]]
    data_mahasiswa[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": hitung_akhir(tugas, uts, uas)}

def hapus():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if data_mahasiswa.pop(nim, None):
        print(f"Data NIM {nim} dihapus.")
    else:
        print("Data tidak ditemukan.")

def cari():
    nim = input("Masukkan NIM: ")
    if mhs := data_mahasiswa.get(nim):
        print(f"\nNama: {mhs['nama']}, Tugas: {mhs['tugas']}, UTS: {mhs['uts']}, UAS: {mhs['uas']}, Akhir: {mhs['akhir']:.2f}")
    else:
        print("Data tidak ditemukan.")

menu = {"l": tampilkan, "t": tambah_ubah, "u": lambda: tambah_ubah(input("NIM yang diubah: ")), "h": hapus, "c": cari}

while True:
    print("\n(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar")
    if (pil := input("Pilih menu: ").lower()) == "k":
        print("Program selesai. Terima kasih!"); break
    menu.get(pil, lambda: print("Pilihan tidak valid"))()
