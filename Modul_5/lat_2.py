#Percobaan 2

#modifikais percobaan 2 untuk menambahkan beberapa variasi
#untuk melengkapi grafik agar lebih informatif dan mudah dipahami
#tunjukan pada asisten bagaimana kalian menambahkan variasi tertentu
#dan dapat mnegubahnya secara langsung


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5, 5))
plt.plot(xpoints, ypoints, color='red', marker='o', label='Garis 1')
plt.xlim([0, 15])
plt.ylim([0, 15])
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Grafik Linier')
plt.legend()
plt.show()