import math

# ============================
# Langkah 1 — Perhitungan Entropi
# ============================

def entropy(keyspace_size: int) -> float: 
    """Menghitung entropi kunci dalam bit."""
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")


# ============================
# Langkah 2 — Unicity Distance
# ============================

def unicity_distance(HK: float, R: float = 0.75, A: int = 26) -> float:
    """Menghitung unicity distance."""
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))


# ============================
# Langkah 3 — Analisis Brute Force
# ============================

def brute_force_time(keyspace_size: int, attempts_per_second: float = 1e6) -> float:
    """
    Menghitung waktu brute force dalam hari.
    keyspace_size: ukuran ruang kunci
    attempts_per_second: jumlah percobaan per detik
    """
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
