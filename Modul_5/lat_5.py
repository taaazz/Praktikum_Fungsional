#Percobaan 5

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Menghasilkan sampel dari distribusi normal
sample = np.random.normal(loc=50, scale=5, size=1000)

plt.figure(figsize=(8, 6))
plt.hist(sample, bins=10, density=True, alpha=0.7, label='Sample Data')  # Menambahkan histogram dari sampel data
plt.xlabel('Nilai')
plt.ylabel('Frekuensi Normalized')

# Menghitung mean dan standard deviation
sample_mean = np.mean(sample)
sample_std = np.std(sample)

# Membuat objek distribusi normal
dist = norm(sample_mean, sample_std)

# Membuat list nilai yang akan digunakan dalam perhitungan
values = [value for value in range(30, 70)]

# Menghitung probabilitas menggunakan metode pdf
probabilitas = [dist.pdf(value) for value in values]

# Menambahkan plot distribusi normal ke histogram
plt.plot(values, probabilitas, label='Distribusi Normal', color='red', linewidth=2)

# Menampilkan hasil
print('Mean=%.3f\nStandard Deviation=%.3f' % (sample_mean, sample_std))
print("\nNilai Probabilitas:")
for value, prob in zip(values, probabilitas):
    print(f"Nilai: {value}, Probabilitas: {prob:.4f}")

# Menambahkan legenda
plt.legend()

plt.show()