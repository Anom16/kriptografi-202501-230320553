# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [judul praktikum]  
Nama: [Nama Mahasiswa]  
NIM: [NIM Mahasiswa]  
Kelas: [Kelas]  

---

## 1. Tujuan
Menyelesaikan operasi aritmetika modular (penjumlahan, pengurangan, perkalian, dan eksponensiasi). Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor) menggunakan algoritma Euclidean. Mengimplementasikan Extended Euclidean Algorithm untuk mencari invers modular. Menerapkan logaritma diskrit sederhana sebagai simulasi konsep dasar dalam kriptografi modern.

---

## 2. Dasar Teori
Aritmetika modular merupakan cabang matematika yang berhubungan dengan operasi aritmetika dalam sistem bilangan yang berulang (modulus). Dalam sistem ini, dua bilangan dikatakan kongruen jika memiliki sisa pembagian yang sama terhadap suatu bilangan modulus 𝑛, Operasi ini menjadi dasar dari banyak algoritma kriptografi modern seperti RSA, Diffie-Hellman, dan ECC.

Greatest Common Divisor (GCD) adalah bilangan bulat terbesar yang dapat membagi dua bilangan tanpa sisa. GCD dapat dihitung dengan algoritma Euclidean, yang bekerja secara efisien melalui proses pembagian berulang. Versi lanjutannya, yaitu Extended Euclidean Algorithm, digunakan untuk mencari invers modular, yang sangat penting dalam kriptografi kunci publik.

Sementara itu, logaritma diskrit adalah permasalahan mencari nilai 𝑥 pada persamaan 𝑎𝑥≡𝑏(mod𝑛) Permasalahan ini sangat sulit diselesaikan ketika modulus 𝑛, sangat besar, dan karena itulah menjadi dasar keamanan berbagai sistem kriptografi modern seperti Diffie–Hellman Key Exchange.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan



---

## 5. Source Code
# ==========================================
# Aritmetika Modular, GCD, Extended Euclid, dan Logaritma Diskrit
# ==========================================
================
Operasi Aritmetika Modular
================
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

==============
(Algoritma Euclidean)
==============
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("=== GCD (Euclidean Algorithm) ===")
print("gcd(54, 24) =", gcd(54, 24))
print()

=====================
Extended Euclidean Algorithm & Invers Modular
====================
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

=============
Logaritma Diskrit (Discrete Log)
=============
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None  # Tidak ditemukan solusi

print("=== Logaritma Diskrit ===")
print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil seharusnya 4
print()

---

## 6. Hasil dan Pembahasan
Hasil :
(![alt text](image-1.png))

Pembahasan
1. Aritmetika Modular
Aritmetika modular menjelaskan bagaimana operasi matematika dilakukan dalam sistem bilangan yang “berputar” setelah mencapai batas tertentu. Misalnya, dengan mod 12, setiap hasil operasi hanya dianggap dalam rentang 0 sampai 11. Jadi ketika 7 + 5 mod 12 = 0, hal itu terjadi karena 7 + 5 = 12, dan 12 dalam sistem mod 12 kembali ke titik awal yaitu 0. Begitu juga 7 * 5 mod 12 = 11, karena 35 dibagi 12 menyisakan 11. Contoh 7^128 mod 13 = 3 menunjukkan bahwa meskipun pangkatnya besar, hasil akhirnya cukup dihitung dari sisa pembagian terhadap 13. Prinsip ini menjadi dasar berbagai algoritma kriptografi karena memungkinkan operasi besar dilakukan dalam ruang bilangan terbatas.

2. Algoritma Euclidean
Algoritma Euclidean digunakan untuk mencari Greatest Common Divisor (GCD), yaitu pembagi terbesar dari dua bilangan. Contohnya, gcd(54, 24) = 6, berarti 6 adalah bilangan terbesar yang dapat membagi 54 dan 24 tanpa sisa. Prosesnya dilakukan dengan membagi bilangan besar dengan bilangan kecil dan mengganti bilangan besar dengan sisa pembagian, terus berulang hingga salah satu menjadi nol. Nilai GCD ini penting dalam teori bilangan dan kriptografi, terutama untuk menentukan apakah dua bilangan saling prima.

3. Algoritma Euclidean yang Diperluas (Extended Euclidean Algorithm)
Versi lanjutan dari algoritma Euclidean tidak hanya mencari GCD, tetapi juga menemukan kombinasi linear antara dua bilangan yang menghasilkan GCD tersebut. Dari kombinasi ini dapat dicari invers modular. Misalnya, invers 3 mod 11 = 4, karena 3 × 4 = 12, dan 12 mod 11 menghasilkan 1. Artinya, 4 adalah invers dari 3 dalam sistem mod 11. Invers modular ini sangat penting dalam sistem enkripsi kunci publik seperti RSA, karena memungkinkan pesan yang telah dienkripsi dapat dikembalikan ke bentuk semula.

4. Logaritma Diskrit
Logaritma diskrit adalah kebalikan dari operasi perpangkatan modular. Dalam contoh 3^x ≡ 4 (mod 7), kita mencari nilai x yang membuat 3 pangkat x menghasilkan sisa 4 saat dibagi 7. Hasilnya x = 4, karena 3⁴ = 81 dan 81 mod 7 = 4. Walaupun sederhana untuk bilangan kecil, pada modulus besar perhitungan logaritma diskrit sangat sulit dibalik. Justru kesulitan inilah yang menjadi dasar keamanan algoritma kriptografi modern seperti Diffie–Hellman dan ElGamal.
---

## 7. Jawaban Pertanyaan

- Pertanyaan 1:Apa peran aritmetika modular dalam kriptografi modern?
Aritmetika modular menjadi dasar sistem kriptografi berbasis teori bilangan seperti RSA, Diffie-Hellman, ElGamal, dan ECC. Ia membatasi ruang bilangan agar operasi tetap efisien secara komputasional, menciptakan struktur siklik yang tidak mudah diprediksi, dan memungkinkan operasi seperti perpangkatan modular yang mudah dihitung tetapi sulit dibalik. Dengan demikian, keamanan sistem kripto tidak bergantung pada kerahasiaan algoritma, melainkan pada sifat matematis fungsi satu arah dalam sistem modular.
- Pertanyaan 2: Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
Invers modular digunakan untuk membentuk kunci privat dalam algoritma RSA. Setelah menentukan nilai e (kunci publik) yang relatif prima terhadap φ(n), maka nilai d dihitung sebagai invers modular dari e terhadap φ(n). Nilai d inilah yang dipakai untuk proses dekripsi, karena memenuhi hubungan matematis:
(m^e)^d ≡ m (mod n)
Artinya, pesan yang sudah dienkripsi dengan kunci publik e dapat dikembalikan ke bentuk aslinya menggunakan d. Tanpa adanya invers modular, proses ini tidak mungkin dilakukan, sehingga invers modular menjadi jembatan penting yang menghubungkan kunci publik dan kunci privat dalam RSA.
- Pertanyaan 3: Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar? 
Masalah logaritma diskrit sulit diselesaikan karena tidak ada algoritma efisien umum untuk menemukan x dari persamaan y = g^x mod p ketika p berukuran besar. Semua metode yang ada, seperti baby-step giant-step, Pollard’s rho, dan index calculus, masih memiliki kompleksitas subeksponensial. Struktur grup yang kompleks, keterbatasan daya komputasi, serta ketahanan terhadap paralelisasi membuat penyelesaiannya sangat sulit. Kesulitan matematis inilah yang menjadi dasar keamanan sistem kriptografi modern berbasis logaritma diskrit.

)
---

## 8. Kesimpulan
Praktikum ini berhasil mengimplementasikan konsep-konsep fundamental matematika kriptografi meliputi aritmetika modular, algoritma Euclidean untuk GCD, Extended Euclidean Algorithm untuk invers modular, dan logaritma diskrit sederhana. Semua fungsi bekerja dengan benar dan memberikan hasil sesuai ekspektasi, menunjukkan pemahaman yang baik terhadap operasi matematika yang menjadi fondasi algoritma kriptografi modern seperti RSA dan Diffie-Hellman.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit anom16
Author:   Anom Pangestu
Date:   2025-11-10

    week3-cryptosystem: modmath-gcd )
```
