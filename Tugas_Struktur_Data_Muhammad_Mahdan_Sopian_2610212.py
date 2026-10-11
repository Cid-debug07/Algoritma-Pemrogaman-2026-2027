mahasiswa = [
    ["2610212", "Mahdan", "Ilmu Komputer"],
    ["2610213", "Hamdi", "Ilmu Komunikasi"],
    ["2610214", "Albar", "Engineering"]
]

def tampilkan_mahasiswa():
    for data in mahasiswa:
        print(data)

#Mengubah data mahasiswa
mahasiswa[0] = ["2610212", "Mahdan", "Ilmu Komputer"]
print("\nSetelah mengubah data:")
tampilkan_mahasiswa()

# menambah data mahasiswa
mahasiswa.append(["2610215", "Rizki", "Informatika"])
print("\nSetelah menambah data:")
tampilkan_mahasiswa()

# menghapus data mahasiswa
del mahasiswa[0]
print("\nSetelah menghapus data:")
tampilkan_mahasiswa()


