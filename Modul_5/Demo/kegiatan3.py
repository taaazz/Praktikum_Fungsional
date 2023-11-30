#Kegiatan 3 (Advance)
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 150, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10

# Todo 1: Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompokkan_ke_interval(data, interval_size):
    return [(x // interval_size) * interval_size for x in data]

# Todo 2: Menghitung frekuensi tinggi badan dalam interval
def hitung_frekuensi(data):
    frekuensi = {}
    for tinggi in data:
        if tinggi in frekuensi:
            frekuensi[tinggi] += 1
        else:
            frekuensi[tinggi] = 1
    return frekuensi

# Mengelompokkan tinggi badan ke dalam interval tertentu
tinggi_interval = kelompokkan_ke_interval(tinggi_badan, interval_size)

# Hitung frekuensi tinggi badan dalam interval
frekuensi_tinggi = hitung_frekuensi(tinggi_interval)

# Todo 3: Visualisasi data dalam bentuk histogram
plt.figure(figsize=(8, 6))
plt.hist(tinggi_badan, bins=np.arange(min(tinggi_badan), max(tinggi_badan) + interval_size, interval_size), color='blue', edgecolor='black')
plt.xlabel('Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Tinggi Badan dalam Interval')
# plt.grid(True)
plt.tight_layout()
plt.show()

# Todo 4: Menambahkan kurva PDF pada hasil visualisasi data
mean = np.mean(tinggi_badan)
std_dev = np.std(tinggi_badan)

x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
kurva_normal = norm.pdf(x, mean, std_dev)

plt.figure(figsize=(8, 6))
plt.hist(tinggi_badan, bins=np.arange(min(tinggi_badan), max(tinggi_badan) + interval_size, interval_size), density=True, color='blue', edgecolor='black', alpha=0.7)
plt.plot(x, kurva_normal, 'r', label='Kurva PDF Normal')
plt.xlabel('Tinggi Badan')
plt.ylabel('Frekuensi / Probabilitas')
plt.title('Histogram dan Kurva PDF Tinggi Badan')
plt.legend()
# plt.grid(True)
plt.tight_layout()
plt.show()
