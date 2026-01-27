# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Aplikasi TLS & E-commerce 
Nama: Anom Pangestu
NIM: 230320553
Kelas: 5DSRA

---

## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada **email** dan **SSL/TLS**.  
2. Menjelaskan enkripsi dalam transaksi **e-commerce**.  
3. Mengevaluasi isu **etika & privasi** dalam penggunaan kriptografi di kehidupan sehari-hari.  
---

## 2. Dasar Teori
Aplikasi TLS (Transport Layer Security) merupakan teknologi keamanan yang digunakan untuk melindungi komunikasi data agar tetap bersifat rahasia, utuh, dan terautentikasi ketika ditransmisikan melalui jaringan publik seperti internet. TLS bekerja dengan mengenkripsi data yang dikirim antara klien dan server, sehingga pihak ketiga tidak dapat membaca atau memodifikasi informasi yang sedang dipertukarkan. Dalam prosesnya, TLS memanfaatkan kriptografi kunci publik, sertifikat digital, serta mekanisme handshake untuk memastikan identitas server dan membangun kunci sesi yang aman.

Dalam konteks e-commerce, TLS memiliki peran yang sangat penting karena transaksi online melibatkan data sensitif seperti informasi pribadi, detail akun, dan data pembayaran pelanggan. Dengan penerapan TLS, data yang dikirim dari browser pengguna ke server e-commerce terlindungi dari serangan penyadapan dan man-in-the-middle. Selain itu, penggunaan sertifikat digital yang valid meningkatkan kepercayaan pengguna karena mereka dapat memastikan bahwa mereka berinteraksi dengan situs yang sah dan bukan situs palsu.

Secara keseluruhan, kombinasi TLS dan sistem e-commerce memungkinkan terciptanya lingkungan transaksi digital yang aman dan tepercaya. Tanpa TLS, risiko kebocoran data dan penipuan akan meningkat secara signifikan, yang dapat merugikan pengguna maupun penyedia layanan. Oleh karena itu, TLS menjadi fondasi utama dalam menjaga keamanan, kepercayaan, dan keberlangsungan aktivitas e-commerce modern.


---

## 3. Alat dan Bahan
1. Buat folder berikut:  
   ```
   praktikum/week12-aplikasi-tls/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Siapkan koneksi internet untuk mengamati penggunaan SSL/TLS (misalnya HTTPS pada browser).  
3. Materi rujukan: Stallings (2017), Bab 15.  


## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
Langkah 1 — Analisis Sertifikat Digital (HTTPS)

Berdasarkan hasil pengamatan pada website e-commerce Blibli dan Tokopedia, keduanya telah menggunakan protokol HTTPS yang didukung oleh sertifikat digital dari DigiCert sebagai Certificate Authority (CA). Sertifikat Blibli diterbitkan oleh DigiCert SHA2 Extended Validation Server CA dengan masa berlaku dari Mei 2025 hingga April 2026, sedangkan Tokopedia menggunakan DigiCert Global G2 TLS RSA SHA256 2020 CA1 dengan masa berlaku dari Juni 2025 hingga Juli 2026.

Algoritma kriptografi yang digunakan meliputi RSA untuk pertukaran kunci dan autentikasi server, SHA-256 untuk integritas data, serta AES untuk enkripsi data selama sesi komunikasi TLS.

Perbedaan utama antara website yang menggunakan HTTPS dan yang tidak menggunakan HTTPS terletak pada keamanan data. HTTPS menjamin kerahasiaan, integritas, dan keaslian data selama transmisi, sedangkan website tanpa HTTPS sangat rentan terhadap penyadapan, manipulasi data, dan pencurian informasi sensitif seperti username dan password.

Langkah 2 — Studi Kasus E-Commerce

Dalam sistem e-commerce, enkripsi digunakan untuk melindungi data pengguna saat proses login, transaksi, dan pembayaran. Protokol TLS memastikan bahwa data yang dikirimkan antara pengguna dan server tidak dapat dibaca atau diubah oleh pihak ketiga. Hal ini sangat penting untuk menjaga keamanan kredensial akun dan informasi pembayaran.

Apabila TLS tidak digunakan, sistem e-commerce berisiko tinggi mengalami serangan seperti Man-in-the-Middle (MITM), di mana penyerang dapat menyadap komunikasi, mencuri data login, atau mengambil alih sesi pengguna. Kondisi ini dapat menyebabkan kerugian finansial dan menurunkan kepercayaan pengguna terhadap platform.

Langkah 3 — Analisis Etika dan Privasi

Dalam penggunaan email terenkripsi seperti PGP dan S/MIME, isu privasi tetap muncul karena meskipun isi email terenkripsi, metadata seperti pengirim dan penerima masih dapat diketahui. Selain itu, pengelolaan kunci enkripsi yang tidak baik dapat menimbulkan risiko kebocoran data.

Dari sisi etika, perusahaan pada prinsipnya boleh melakukan dekripsi email karyawan untuk keperluan audit keamanan, dengan syarat telah diatur secara transparan dalam kebijakan internal dan hanya berlaku untuk akun email resmi perusahaan. Sementara itu, pengawasan pemerintah terhadap komunikasi terenkripsi menimbulkan dilema antara keamanan nasional dan hak privasi masyarakat, karena pelemahan enkripsi berpotensi membahayakan keamanan data secara keseluruhan.

---

## 7. Jawaban Pertanyaan
1. Perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP mengirimkan data dalam bentuk teks biasa sehingga mudah disadap atau dimodifikasi oleh pihak ketiga, sedangkan HTTPS menggunakan TLS untuk mengenkripsi komunikasi antara klien dan server. Dengan HTTPS, data menjadi lebih aman karena kerahasiaan, integritas, dan keaslian komunikasi dapat terjamin.

2. Sertifikat digital penting dalam komunikasi TLS karena berfungsi untuk memverifikasi identitas server yang diakses oleh pengguna. Sertifikat ini diterbitkan oleh Certificate Authority (CA) tepercaya dan mengikat identitas pemilik situs dengan kunci publiknya. Dengan adanya sertifikat digital, pengguna dapat memastikan bahwa mereka berkomunikasi dengan server yang sah dan bukan dengan pihak palsu yang mencoba melakukan penipuan atau serangan man-in-the-middle.

3. Kriptografi mendukung privasi dalam komunikasi digital dengan melindungi data agar hanya dapat dibaca oleh pihak yang berwenang, sehingga informasi pribadi dan transaksi sensitif tetap aman. Namun, penggunaan kriptografi juga menimbulkan tantangan hukum dan etika, karena enkripsi yang kuat dapat menyulitkan penegak hukum dalam mengakses data untuk kepentingan investigasi. Hal ini menimbulkan perdebatan antara perlindungan privasi individu dan kebutuhan negara dalam menjaga keamanan serta penegakan hukum.


## 8. Kesimpulan
**Kesimpulan**

Penggunaan protokol HTTPS yang didukung oleh sertifikat digital dan enkripsi TLS merupakan fondasi utama dalam menjaga keamanan komunikasi data di internet, khususnya pada platform e-commerce. Melalui mekanisme enkripsi, autentikasi server, dan penjagaan integritas data, HTTPS mampu melindungi informasi sensitif pengguna seperti kredensial login dan data transaksi dari ancaman penyadapan maupun manipulasi data selama proses transmisi.

Namun, keamanan teknis tidak dapat berdiri sendiri tanpa dukungan kebijakan dan etika yang jelas. Pada komunikasi terenkripsi seperti email, isu privasi, pengelolaan kunci, serta akses pihak berwenang menjadi tantangan yang harus diatur secara transparan dan proporsional. Oleh karena itu, penerapan enkripsi yang kuat perlu diimbangi dengan kebijakan keamanan informasi yang bertanggung jawab agar keamanan sistem dan perlindungan privasi dapat berjalan seimbang dan berkelanjutan.
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

    week12-cryptosystem: )
```
