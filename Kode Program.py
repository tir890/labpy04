data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama       : ")
    nim = input("NIM        : ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS  : "))
    uas = float(input("Nilai UAS  : "))
    
    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)
    
    data_mahasiswa.append({
        'nama': nama,
        'nim': nim,
        'tugas': tugas,
        'uts': uts,
        'uas': uas,
        'nilai_akhir': nilai_akhir
    })
    
    tambah = input("Tambah data lagi (y/t)? ").lower()
    if tambah == 't':
        break

print("\nData Mahasiswa:")
print("="*73)
print(f"| {'No':^2} | {'Nama':^15} | {'NIM':^10} | {'Tugas':^6} | {'UTS':^6} | {'UAS':^6} | {'Akhir':^6} |")
print("="*73)
for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"| {i:^2} | {mhs['nama']:^15} | {mhs['nim']:^10} | {mhs['tugas']:^6.2f} | {mhs['uts']:^6.2f} | {mhs['uas']:^6.2f} | {mhs['nilai_akhir']:^6.2f} |")
print("="*73)
