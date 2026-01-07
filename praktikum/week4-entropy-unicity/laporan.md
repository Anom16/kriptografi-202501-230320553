# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: Entropy & Unicity Distance
Nama: Anom Pangestu
NIM: 230320553  
Kelas: 5DSRA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.  
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.  
3. Menghitung **unicity distance** untuk ciphertext tertentu.  
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.  
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana. 

---

## 2. Dasar Teori
Selain itu, dasar teori ini juga menegaskan bahwa keamanan cipher tidak hanya ditentukan oleh ukuran ruang kunci, tetapi juga oleh bagaimana informasi mengalir dan bagaimana kunci serta plaintext diproses oleh sistem. Shannon memperkenalkan prinsip **confusion** dan **diffusion** sebagai dua mekanisme inti untuk menyamarkan hubungan antara plaintext, ciphertext, dan kunci. Confusion bertujuan membuat hubungan antara kunci dan ciphertext menjadi sangat kompleks, sementara diffusion menyebarkan informasi plaintext ke seluruh ciphertext agar pola tidak mudah terlihat. Cipher modern seperti AES dirancang dengan struktur matematis yang memaksimalkan kedua prinsip ini sehingga pola plaintext tidak memberikan petunjuk bagi penyerang, sekaligus menjaga entropi efektif kunci tetap tinggi.

Di samping aspek teoritis, relevansi konsep-konsep ini perlu ditempatkan dalam konteks serangan modern. Unicity distance, misalnya, merupakan batas teoretis untuk penyerang dengan kemampuan tak terbatas. Dalam praktiknya, serangan lebih sering melewati jalur implementasi, bukan matematika cipher: kesalahan penggunaan nonce, kelemahan RNG, kebocoran side-channel, atau password yang tidak acak dapat menurunkan entropi efektif secara drastis. Dengan kata lain, meskipun sebuah cipher memiliki entropi kunci besar dan unicity distance yang sangat tinggi, sistem tetap dapat runtuh jika faktor-faktor pendukungnya lemah. Karena itu, teori Shannon penting bukan hanya untuk memahami batas matematis cipher, tetapi juga untuk menyadarkan bahwa keamanan bergantung pada keseluruhan ekosistem, bukan formula tunggal.


---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Membuat struktur folder proyek `praktikum/week4-entropy-unicity/` yang berisi sub-folder `src/` dan `screenshots/`, serta file `laporan.md`.
2. Membuat file Python baru bernama `entropy_unicity.py` di dalam folder `src/`.
3. Mengimplementasikan tiga fungsi Python di dalam file tersebut sesuai panduan, yaitu:
    a. entropy` untuk menghitung entropi kunci,
    b. unicity_distance` untuk menghitung unicity distance,
    c. brute_force_time` untuk mengestimasi waktu serangan brute force.
4. Menambahkan blok `if __name__ == "__main__":` untuk menjalankan perhitungan pada dua kasus, termasuk Caesar Cipher.
5. Menjalankan program dari terminal menggunakan perintah: `python src/entropy_unicity.py`.
6. Mengambil screenshot dari output terminal dan menyimpannya sebagai `screenshots/hasil.png`.
7. Melengkapi file `laporan.md` dengan seluruh bagian yang diminta, termasuk jawaban pertanyaan diskusi.
8. Melakukan commit dan push ke repositori GitHub dengan pesan commit `week4-entropy-unicity`.

---

## 5. Source Code
#Perhitungan Entropi
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

#Menghitung Unicity Distance
def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

#Analisis Brute Force
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
---

## 6. Hasil dan Pembahasan


---

## 7. Jawaban Pertanyaan

1. Entropy dalam konteks kekuatan kunci berarti tingkat ketidakpastian atau jumlah informasi yang dibutuhkan untuk menebak kunci, sehingga semakin tinggi entropinya semakin sulit kunci ditebak—namun nilai ini hanya bermakna jika kunci benar-benar acak dan implementasinya tidak bocor.

2. Unicity distance penting karena menunjukkan berapa banyak ciphertext yang dibutuhkan agar hanya satu kunci yang mungkin cocok, sehingga ia menjadi batas teoritis di mana redundansi plaintext membuat cipher dapat dipecahkan bila cukup data tersedia.

3. Brute force tetap menjadi ancaman karena kelemahan biasanya bukan pada algoritma, melainkan pada password yang tidak acak, implementasi yang buruk, kelemahan sistem pendukung, dan perkembangan hardware yang membuat pencarian kunci semakin cepat sehingga ruang kunci efektif sering lebih kecil dari yang dikira.

---

## 8. Kesimpulan
Praktikum ini menunjukkan bagaimana mengevaluasi kekuatan kriptosistem secara kuantitatif menggunakan entropi kunci, unicity distance, dan estimasi waktu brute force. Melalui perhitungan, terbukti bahwa cipher klasik seperti Caesar Cipher memiliki entropi yang sangat rendah (4.7 bit) dan dapat dipecahkan secara instan. Sebaliknya, kriptosistem modern seperti AES-128 memiliki entropi 128 bit, yang menyediakan ruang kunci sangat besar (2^128) sehingga membuatnya aman dari serangan brute force untuk waktu yang sangat lama.
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit jbjsxsxnksxxm 
Author: Anom Pangestu <@gmail.com>  
Date:   2025-11-04  

   week4-entropy-unicity  
```
