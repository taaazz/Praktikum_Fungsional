# Fungsi untuk menambahkan buku baru
def tambah_buku(database_buku, judul, penulis):
    buku = {"ID": len(database_buku), "Judul": judul, "Penulis": penulis, "Status": "Tersedia"}
    return database_buku + [buku], "Buku '{}' oleh {} telah ditambahkan.".format(judul, penulis)

# Fungsi untuk menampilkan buku-buku yang tersedia
def tampilkan_buku_tersedia(database_buku):
    buku_tersedia = [buku for buku in database_buku if buku["Status"] == "Tersedia"]
    for buku in buku_tersedia:
        print("ID: {}, Judul: {}, Penulis: {}".format(buku["ID"], buku["Judul"], buku["Penulis"]))

# Fungsi untuk meminjam buku
def pinjam_buku(database_buku, database_peminjaman, id_buku, id_user):
    buku = next((b for b in database_buku if b["ID"] == id_buku and b["Status"] == "Tersedia"), None)
    if buku:
        buku["Status"] = "Dipinjam oleh User {}".format(id_user)
        peminjaman = {"ID Buku": id_buku, "ID User": id_user}
        return database_buku, database_peminjaman + [peminjaman], "Buku '{}' berhasil dipinjam.".format(buku["Judul"])
    else:
        return database_buku, database_peminjaman, "Buku dengan ID {} tidak ditemukan atau sudah dipinjam.".format(id_buku)

# Fungsi untuk mengembalikan buku
def kembalikan_buku(database_buku, database_peminjaman, id_buku, id_user):
    peminjaman = next((p for p in database_peminjaman if p["ID Buku"] == id_buku and p["ID User"] == id_user), None)
    if peminjaman:
        buku = next(b for b in database_buku if b["ID"] == id_buku)
        buku["Status"] = "Tersedia"
        return database_buku, [p for p in database_peminjaman if p != peminjaman], "Buku '{}' berhasil dikembalikan.".format(buku["Judul"])
    else:
        return database_buku, database_peminjaman, "Data peminjaman tidak ditemukan."

if __name__ == "__main__":
    database_buku = []
    database_peminjaman = []

    while True:
        print("\nSelamat datang di Sistem Peminjaman Buku")
        print("1. Login sebagai Admin")
        print("2. Login sebagai User")
        print("3. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            print("\nLogin sebagai Admin")
            username = input("Username: ")
            password = input("Password: ")

            while True:
                print("\nMenu Admin:")
                print("1. Tambah Buku")
                print("2. Lihat Buku Tersedia")
                print("3. Keluar")

                admin_pilihan = input("Pilih opsi: ")

                if admin_pilihan == "1":
                    judul = input("Judul Buku: ")
                    penulis = input("Penulis Buku: ")
                    database_buku, message = tambah_buku(database_buku, judul, penulis)
                    print(message)
                elif admin_pilihan == "2":
                    tampilkan_buku_tersedia(database_buku)
                elif admin_pilihan == "3":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == "2":
            print("\nLogin sebagai User")
            user_id = input("Masukkan ID User: ")

            while True:
                print("\nMenu User:")
                print("1. Pinjam Buku")
                print("2. Kembalikan Buku")
                print("3. Keluar")

                user_pilihan = input("Pilih opsi: ")

                if user_pilihan == "1":
                    tampilkan_buku_tersedia(database_buku)
                    id_buku_pinjam = int(input("Masukkan ID Buku yang ingin dipinjam: "))
                    database_buku, database_peminjaman, message = pinjam_buku(database_buku, database_peminjaman, id_buku_pinjam, user_id)
                    print(message)
                elif user_pilihan == "2":
                    tampilkan_buku_tersedia(database_buku)
                    id_buku_kembali = int(input("Masukkan ID Buku yang ingin dikembalikan: "))
                    database_buku, database_peminjaman, message = kembalikan_buku(database_buku, database_peminjaman, id_buku_kembali, user_id)
                    print(message)
                elif user_pilihan == "3":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
