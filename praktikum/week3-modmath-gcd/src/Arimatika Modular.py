# ==========================================
# Aritmetika Modular, GCD, Extended Euclid, dan Logaritma Diskrit
# ==========================================

# 1. Operasi Aritmetika Modular
def mod_add(a, b, n): 
    return (a + b) % n

def mod_sub(a, b, n): 
    return (a - b) % n

def mod_mul(a, b, n): 
    return (a * b) % n

def mod_exp(base, exp, n): 
    return pow(base, exp, n)  # eksponensiasi modular efisien

print("=== Aritmetika Modular ===")
print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))
print()


# 2. GCD (Algoritma Euclidean)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("=== GCD (Euclidean Algorithm) ===")
print("gcd(54, 24) =", gcd(54, 24))
print()


# 3. Extended Euclidean Algorithm & Invers Modular
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None  # Tidak ada invers jika gcd != 1
    return x % n

print("=== Extended Euclidean & Invers Modular ===")
print("Invers 3 mod 11 =", modinv(3, 11))  # hasil seharusnya 4
print()


# 4. Logaritma Diskrit (Discrete Log)
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None  # Tidak ditemukan solusi

print("=== Logaritma Diskrit ===")
print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil seharusnya 4
print()
