import math

# Decorator untuk translasi
def translasi_decorator(func):
    def wrapper(x, y):
        new_x, new_y = func(x, y)
        new_x += 2
        new_y -= 3
        return new_x, new_y
    return wrapper

# Decorator untuk rotasi sejajar sumbu x
def rotasi_decorator(func):
    def wrapper(x, y):
        sudut = math.radians(60)  # Rotasi 60 derajat sejajar sumbu x
        new_x, new_y = func(x, y)
        new_x_rotated = new_x * math.cos(sudut) - new_y * math.sin(sudut)
        new_y_rotated = new_x * math.sin(sudut) + new_y * math.cos(sudut)
        return new_x_rotated, new_y_rotated
    return wrapper

# Decorator untuk dilatasi
def dilatasi_decorator(func):
    def wrapper(x, y):
        new_x, new_y = func(x, y)
        new_x *= 1.5  # Dilatasi 1.5 pada sumbu x
        new_y *= 2    # Dilatasi 2 pada sumbu y
        return new_x, new_y
    return wrapper

# Fungsi titik
def point(x, y):
    return x, y

# Fungsi persamaan garis
def line_equation_of(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1

    return m, c

# Transformasi gabungan dengan decorator
@dilatasi_decorator
@rotasi_decorator
@translasi_decorator
def combined_transform(x, y):
    return x, y

# Input nilai x, y, z dari pengguna
x = float(input("Masukkan nilai x untuk titik A: "))
y = float(input("Masukkan nilai y untuk titik A: "))
z = float(input("Masukkan nilai z untuk titik B: "))

# Hitung transformasi sesuai urutan yang diminta
titik_transformed_A = combined_transform(x, y)
titik_transformed_B = combined_transform(y, z)

# Cari persamaan garis yang melalui titik hasil transformasi
m_gradient = x  # Gradien yang diberikan oleh pengguna
print(f"Persamaan garis yang melalui titik ({x},{y}) dan memiliki gradien {m_gradient}:")
transformed_A = combined_transform(x, y)
transformed_B = combined_transform(y, z)
transformed_m, transformed_c = line_equation_of(transformed_A, transformed_B)
print(f"y = {transformed_m:.2f}x + {transformed_c:.2f}")

transformed_m_gradient, transformed_c_gradient = line_equation_of(combined_transform(x, y), combined_transform(y, m_gradient))
print(f"Persamaan garis yang baru setelah transformasi:")
print(f"y = {transformed_m_gradient:.2f}x + {transformed_c_gradient:.2f}")


# Hitung transformasi pada garis CD yang berasal dari input x, y, z
titik_C = point(x, y)
titik_D = point(y, z)
garis_CD_transformed = combined_transform(x, y)  # Transformasi garis CD

# Cetak persamaan garis yang baru setelah transformasi
m_CD, c_CD = line_equation_of(titik_C, titik_D)
print(f"Persamaan garis yang melalui titik ({x},{y}) dan ({y},{z}):")
print(f"y = {m_CD:.2f}x + {c_CD:.2f}")
m_CD_transformed, c_CD_transformed = line_equation_of(garis_CD_transformed, combined_transform(y, z))
print("Persamaan garis yang baru setelah transformasi :")
print(f"y = {m_CD_transformed:.2f}x + {c_CD_transformed:.2f}")
