def point(x, y):
    return x, y

def line_equation_of(p1, M):
    # Menghitung nilai C
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

# Point (7,7) dan gradien 2
point_p1 = point(7, 7)
gradien_M = 2

# Mendapatkan persamaan garis lurus
persamaan_garis = line_equation_of(point_p1, gradien_M)

print("Persamaan garis yang melalui titik (7,7) dan bergradien 2:")
print(persamaan_garis)
