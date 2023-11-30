#Kegiatan 2 (Intermediate)

import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10), 
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15), 
    ("Produk F", 70, 5), 
]

# Todo 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = [item[1] for item in data_transaksi]
jumlah_terjual = [item[2] for item in data_transaksi]

# Todo 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(8, 6))
plt.scatter(harga_produk, jumlah_terjual, color='blue', marker='o')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Terjual')
plt.grid(True)
plt.tight_layout()
plt.show()

# Todo 3: Hitung total pendapatan untuk setiap produk
total_pendapatan = list(map(lambda x: x[1] * x[2], data_transaksi))

# Todo 4: Tambahkan bar chart untuk menampilkan pendapatan produk
produk = [item[0] for item in data_transaksi]
x = np.arange(len(produk))

plt.figure(figsize=(8, 6))
plt.bar(x, total_pendapatan, color='green')
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan Produk ')
plt.title('Pendapatan Produk')
plt.xticks(x, produk)
plt.tight_layout()
plt.show()
