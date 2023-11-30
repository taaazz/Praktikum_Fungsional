def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# example hof
def kurangi_100(a):
    return a - 100

result = kurangi_100(200)
print(result)

# example currying
kali_dua = perkalian(2)
hasil = kali_dua(11)
print(hasil)
