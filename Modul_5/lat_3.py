#Percobaan 3

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 9, 4, 8])

plt.plot(y1, label='Garis 1', linestyle='-', color='blue')
plt.plot(y2, label='Garis 2', linestyle='--', color='green')
plt.plot(y3, label='Garis 3', linestyle=':', color='red')

plt.title('Plot Tiga Garis')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.legend()

plt.show()

#modifikasi percobaan 3 untuk menggambar 3/lebih  garis
#dengan corak garis yang berbeda-beda
#tunjukan pada asisten bagaimana kalian menambahkan garis
#mengubah corak garis secara langsung