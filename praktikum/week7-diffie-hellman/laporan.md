# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Diffie Hellman
Nama: Anom Pangestu
NIM: 230320553  
Kelas: 5DSRA  

---

## 1. Tujuan
1. Melakukan simulasi protokol **Diffie-Hellman** untuk pertukaran kunci publik.  
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.  
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan **Man-in-the-Middle / MITM**)
---

## 2. Dasar Teori
Diffie–Hellman merupakan protokol kriptografi yang digunakan untuk memungkinkan dua pihak bertukar kunci rahasia melalui jaringan publik tanpa harus mengirimkan kunci tersebut secara langsung. Protokol ini dirancang untuk mengatasi risiko penyadapan yang dapat terjadi apabila kunci rahasia dikirimkan secara terbuka melalui jaringan.

Dasar teori Diffie–Hellman bertumpu pada konsep fungsi satu arah dan masalah logaritma diskret, yaitu perhitungan yang mudah dilakukan ke satu arah tetapi sangat sulit dibalik. Dengan memanfaatkan parameter publik dan nilai rahasia privat yang dimiliki masing-masing pihak, protokol ini memungkinkan kedua pihak menghasilkan kunci akhir yang sama meskipun hanya bertukar nilai perantara.

Diffie–Hellman bukan merupakan algoritma enkripsi, melainkan protokol untuk pertukaran kunci. Kunci yang dihasilkan dari proses ini selanjutnya digunakan oleh algoritma kriptografi lain untuk mengamankan data yang dipertukarkan. Selain itu, protokol ini tidak menyediakan mekanisme autentikasi identitas, sehingga dalam penerapan praktis perlu dikombinasikan dengan sistem keamanan tambahan agar komunikasi dapat berlangsung secara aman.


---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Langkah-langkah simulasi Diffie–Hellman disesuaikan dengan contoh tersebut adalah sebagai berikut.

1. Menuliskan kode program simulasi Diffie–Hellman menggunakan bahasa Python, yang mencakup penentuan parameter publik, pembuatan kunci privat, perhitungan kunci publik, serta pembentukan kunci bersama.

2. Menjalankan program menggunakan perintah `diffie_hellman.py` melalui terminal atau command prompt.

3. Mengamati hasil keluaran program untuk memastikan bahwa nilai kunci bersama yang dihasilkan oleh kedua pihak bernilai sama.

4. Memodifikasi program dengan menambahkan skenario serangan man-in-the-middle, kemudian menjalankan kembali program untuk melihat perbedaan kunci yang dihasilkan dan menganalisis implikasi keamanannya.

---

## 5. Source Code
Panduan Langkah demi Langkah

### Langkah 1 — Simulasi Diffie-Hellman
```python
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```

Ekspektasi hasil: nilai `shared_secret_A` dan `shared_secret_B` harus sama.

---

## 6. Hasil dan Pembahasan
Mekanisme Diffie–Hellman bekerja dengan memungkinkan dua pihak membentuk kunci rahasia yang sama melalui saluran komunikasi publik tanpa pernah mengirimkan kunci tersebut secara langsung. Proses ini dimulai dengan penetapan parameter publik berupa sebuah bilangan prima dan sebuah generator yang dapat diketahui oleh siapa pun. Selanjutnya, masing-masing pihak memilih nilai rahasia privat yang tidak dibagikan. Berdasarkan parameter publik dan nilai rahasia ini, setiap pihak menghitung kunci publiknya dan menukarkannya melalui jaringan. Setelah pertukaran kunci publik dilakukan, masing-masing pihak mengombinasikan kunci publik yang diterima dengan nilai rahasia privatnya sendiri untuk menghasilkan kunci bersama. Karena sifat matematis dari operasi yang digunakan, hasil akhir yang diperoleh oleh kedua pihak akan sama meskipun perhitungannya dilakukan secara terpisah.

Berdasarkan hasil simulasi yang diperoleh, yaitu kunci bersama Alice bernilai 4 dan kunci bersama Bob juga bernilai 4, dapat disimpulkan bahwa mekanisme Diffie–Hellman berjalan dengan benar. Kesamaan nilai kunci bersama menunjukkan bahwa proses pertukaran kunci berhasil dan kedua pihak telah menghasilkan kunci rahasia yang identik tanpa perlu mengirimkan kunci tersebut secara langsung. Hasil ini sekaligus membuktikan bahwa pihak luar yang hanya mengetahui parameter publik dan kunci publik tidak dapat dengan mudah menurunkan kunci rahasia yang dihasilkan.

---

## 7. Jawaban Pertanyaan
1. Diffie–Hellman memungkinkan pertukaran kunci di saluran publik karena protokol ini tidak pernah mengirimkan kunci rahasia secara langsung. Yang dipertukarkan hanyalah parameter publik dan nilai hasil perhitungan sementara, sementara kunci akhir dibentuk secara mandiri oleh masing-masing pihak menggunakan nilai rahasia privat. Keamanan proses ini bergantung pada kesulitan matematis dalam memecahkan masalah logaritma diskret, sehingga pihak ketiga yang menyadap tidak dapat menurunkan kunci rahasia dari informasi publik yang tersedia.

2. Kelemahan utama protokol Diffie–Hellman murni adalah tidak adanya mekanisme autentikasi identitas. Protokol ini tidak dapat memastikan bahwa pihak yang diajak berkomunikasi benar-benar pihak yang dimaksud. Akibatnya, Diffie–Hellman rentan terhadap serangan man-in-the-middle, di mana penyerang dapat mencegat dan mengganti kunci publik tanpa terdeteksi.

3. Serangan man-in-the-middle pada Diffie–Hellman dapat dicegah dengan menambahkan mekanisme autentikasi. Cara yang umum digunakan adalah mengombinasikan Diffie–Hellman dengan sertifikat digital, tanda tangan kriptografi, atau protokol keamanan seperti TLS. Dengan autentikasi ini, identitas masing-masing pihak dapat diverifikasi sehingga pertukaran kunci tidak dapat dimanipulasi oleh pihak ketiga.

---

## 8. Kesimpulan
Berdasarkan simulasi dan pembahasan yang telah dilakukan, dapat disimpulkan bahwa protokol Diffie–Hellman mampu memfasilitasi pembentukan kunci rahasia bersama melalui saluran komunikasi publik tanpa harus mengirimkan kunci tersebut secara langsung. Kesamaan nilai kunci bersama yang dihasilkan oleh Alice dan Bob menunjukkan bahwa mekanisme pertukaran kunci berjalan dengan benar sesuai dengan prinsip matematis yang mendasarinya.

Namun demikian, meskipun aman dari penyadapan pasif, Diffie–Hellman murni memiliki keterbatasan karena tidak menyediakan autentikasi identitas. Oleh sebab itu, dalam penerapan nyata, protokol ini perlu dikombinasikan dengan mekanisme keamanan tambahan agar komunikasi tidak rentan terhadap serangan aktif seperti man-in-the-middle.

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
commit anom
Author: Anom Pangestu
Date:   2026-01

    week7-cryptosystem: diffie hellman )
```
