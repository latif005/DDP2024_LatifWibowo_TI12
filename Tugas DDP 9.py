# Nomer 1
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

# Contoh penggunaan
print(celcius_ke_fahrenheit(0))    # Output: 32.0
print(celcius_ke_fahrenheit(100))  # Output: 212.0

# Nomer 2
def is_genap(bilangan):
    return bilangan % 2 == 0

# Contoh penggunaan
print(is_genap(4))  # Output: True
print(is_genap(7))  # Output: False

# Nomer 3
def nilai(angka):
    if angka >= 70:
        return "Lulus"
    else:
        return "Gagal"

# Contoh penggunaan
print(nilai(80))  # Output: Lulus
print(nilai(60))  # Output: Gagal

# Nomer 4
def bilangan(n):
    return [i for i in range(1, n, 2)]

# Contoh penggunaan
print(bilangan(20))  # Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
