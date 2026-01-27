# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Analisis Serangan Kriptografi 
Nama: Anom Pangestu
NIM: 230320553
Kelas: 5DSRA


---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.  
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.  
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.  
---

## 2. Dasar Teori

Analisis serangan kriptografi merupakan kajian untuk memahami berbagai metode yang digunakan penyerang dalam melemahkan atau menembus sistem kriptografi. Tujuan utama dari analisis ini adalah mengidentifikasi kelemahan pada algoritma, implementasi, atau pengelolaan kunci yang dapat dimanfaatkan untuk memperoleh informasi rahasia tanpa izin. Serangan kriptografi tidak selalu menargetkan algoritma itu sendiri, tetapi juga dapat memanfaatkan kesalahan konfigurasi dan perilaku pengguna.

Secara umum, serangan kriptografi dapat diklasifikasikan menjadi beberapa jenis, seperti *ciphertext-only attack*, *known-plaintext attack*, dan *chosen-plaintext attack*, yang berfokus pada analisis hubungan antara plaintext dan ciphertext. Selain itu, terdapat serangan berbasis implementasi, seperti *side-channel attack*, yang memanfaatkan informasi fisik dari proses enkripsi, misalnya waktu komputasi atau konsumsi daya, untuk mengekstraksi kunci rahasia.

Pemahaman terhadap analisis serangan kriptografi sangat penting dalam perancangan sistem keamanan informasi, karena memungkinkan pengembang untuk memilih algoritma yang kuat, menerapkan konfigurasi yang aman, serta melakukan mitigasi terhadap potensi ancaman. Dengan analisis yang tepat, sistem kriptografi dapat dirancang agar tetap aman meskipun penyerang mengetahui algoritma yang digunakan, sesuai dengan prinsip keamanan kriptografi modern.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Buat folder berikut:  
   ```
   praktikum/week14-analisis-serangan/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Diskusikan studi kasus sistem nyata (contoh: serangan brute force pada password lemah, serangan MITM pada komunikasi TLS, serangan replay pada protokol autentikasi).  
3. Materi rujukan: Stallings (2017), Bab 16.  
---

## 5. Source Code


## 6. Hasil dan Pembahasan
Identifikasi Serangan
Salah satu contoh kasus nyata adalah serangan brute force dan collision pada algoritma hash MD5. Vektor serangan berasal dari kemampuan penyerang untuk menghasilkan hash yang sama (collision) atau menebak nilai asli melalui dictionary attack. Penyebab utama kelemahan ini adalah desain algoritma MD5 yang sudah tidak aman secara kriptografis dan tidak lagi mampu menahan perkembangan daya komputasi modern.

Evaluasi Kelemahan
Kelemahan pada kasus ini terutama terletak pada algoritma kriptografinya. MD5 memiliki panjang hash yang pendek dan telah terbukti rentan terhadap collision attack, sehingga secara teori maupun praktik tidak lagi aman. Selain itu, dalam banyak sistem lama, MD5 juga sering diimplementasikan tanpa mekanisme tambahan seperti salt, yang semakin memperparah risiko serangan brute force dan dictionary.

Rekomendasi Solusi
Solusi yang direkomendasikan adalah mengganti MD5 dengan algoritma yang lebih kuat seperti SHA-256 atau SHA-3 untuk kebutuhan hashing umum, serta menggunakan bcrypt, scrypt, atau Argon2 untuk penyimpanan password. Algoritma tersebut dirancang lebih tahan terhadap brute force karena memiliki proses komputasi yang lebih mahal dan mendukung penggunaan salt. Dampaknya, keamanan sistem meningkat secara signifikan karena penyerang membutuhkan sumber daya dan waktu yang jauh lebih besar untuk melakukan serangan.

---

## 7. Jawaban Pertanyaan
1. Banyak sistem lama masih rentan terhadap brute force atau dictionary attack karena menggunakan algoritma kriptografi yang sudah usang, panjang kunci yang pendek, atau mekanisme penyimpanan kata sandi yang lemah seperti hashing tanpa salt. Selain itu, sistem lama sering tidak diperbarui secara rutin sehingga tetap mempertahankan konfigurasi keamanan yang sudah tidak sesuai dengan standar keamanan saat ini.

2. Kelemahan algoritma berkaitan dengan desain matematis atau konsep dasar dari algoritma kriptografi itu sendiri, misalnya algoritma yang telah terbukti dapat dipecahkan secara teoritis atau praktis. Sementara itu, kelemahan implementasi muncul akibat kesalahan dalam penerapan algoritma, seperti penggunaan kunci yang buruk, manajemen kunci yang tidak aman, atau kesalahan pemrograman, meskipun algoritma yang digunakan secara teori masih kuat.

3. Organisasi dapat memastikan sistem kriptografi tetap aman di masa depan dengan selalu mengikuti standar dan rekomendasi terbaru, melakukan pembaruan sistem secara berkala, serta menggunakan algoritma dan panjang kunci yang dianggap aman oleh komunitas kriptografi. Selain itu, audit keamanan, pengujian berkala, dan peningkatan kesadaran keamanan bagi pengembang dan pengguna juga penting untuk mengantisipasi ancaman baru yang terus berkembang.

---

## 8. Kesimpulan

Kasus serangan brute force dan collision pada MD5 menunjukkan bahwa penggunaan algoritma kriptografi yang sudah usang dan implementasi yang lemah dapat menimbulkan risiko keamanan yang serius. Kelemahan ini menegaskan pentingnya pemilihan algoritma yang kuat serta penerapan mekanisme tambahan seperti salt untuk mencegah serangan. Oleh karena itu, penggunaan algoritma modern dan pembaruan sistem keamanan secara berkala menjadi langkah penting untuk menjaga ketahanan sistem kriptografi terhadap ancaman yang terus berkembang.

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
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
