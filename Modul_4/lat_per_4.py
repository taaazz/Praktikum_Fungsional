import math

def translasi(x, y, tx, ty):
    new_x = x + tx
    new_y = y + ty
    return new_x, new_y

def dilatasi(x, y, sx, sy):
    new_x = x * sx
    new_y = y * sy
    return new_x, new_y

def rotasi(x, y, sudut):
    sudut_rad = math.radians(sudut)
    new_x = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
    new_y = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
    return new_x, new_y

# Contoh penggunaan
titik_awal = (3, 5)

# Translasi
tx, ty = 2, -1
titik_setelah_translasi = translasi(titik_awal[0], titik_awal[1], tx, ty)
print(f"Titik setelah translasi: {titik_setelah_translasi}")

# Dilatasi
sx, sy = 2, -1
titik_setelah_dilatasi = dilatasi(titik_awal[0], titik_awal[1], sx, sy)
print(f"Titik setelah dilatasi: {titik_setelah_dilatasi}")

# Rotasi
sudut_rotasi = 30
titik_setelah_rotasi = rotasi(titik_awal[0], titik_awal[1], sudut_rotasi)
print(f"Titik setelah rotasi: {titik_setelah_rotasi}")
