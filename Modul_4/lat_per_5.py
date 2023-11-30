def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_M(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    # Memanggil inner function untuk meendapatkan nilai M
    M = calculate_M(p1, p2)

    # Menghitung nilai C
    C = p1[1] - M * p1[0]
    return f"y = {M:.2f}x + {C:.2f}"

# Titik A dan B
point_A = point(1, 2)
point_B = point(7, 7)

# Mendapatkan persamaan garis lurus
persamaan_AB = line_equation_of(point_A, point_B)

print("Persamaan garis yang melalui titik A dan B:")
print(persamaan_AB)
