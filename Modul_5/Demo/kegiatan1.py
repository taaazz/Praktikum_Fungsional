#Kegiatan 1 (Beginner)
import matplotlib.pyplot as plt
from functools import reduce

# Data Nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata menggunakan fungsi reduce
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)
print("Rata-rata nilai mahasiswa:", rata_rata)

# Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lambda)
label_mahasiswa = list(map(lambda x: f"Mahasiswa {x+1}", range(len(nilai_mahasiswa))))

# Visualisasi data dalam bentuk diagram batang
plt.figure(figsize=(8, 6))
plt.bar(label_mahasiswa, nilai_mahasiswa, color='skyblue', label='Nilai Mahasiswa')
plt.axhline(rata_rata, color='red', linestyle='--', label='Rata-rata')  # Menambah garis rata-rata
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Mahasiswa')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
