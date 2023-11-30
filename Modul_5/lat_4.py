#Percobaan 4
#pastikan kalian sudah melakukan import library dengan plt alis 
#sebelum menjalankan kode ini

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

colors = ['red', 'green', 'blue', 'purple', 'orange']
sizes = [20, 50, 100, 150, 200]

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, edgecolors='black', linewidth=1.5, label='Data Points')

plt.title('Scatter Plot dengan Variasi')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.legend()

plt.show()

#modifikasi percobaan 4 dengan menambahkan variasi baru
#tunjukan pada asistensi variasi apa saja yang kalian buat