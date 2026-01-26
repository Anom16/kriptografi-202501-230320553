# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Public Key Infrastructure (PKI & Certificate Authority) 
Nama: Anom Pangestu
NIM: 230320553 
Kelas: 5DSRA  

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.  
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.  
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).  
---

## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan suatu kerangka kerja keamanan yang digunakan untuk mengelola penggunaan kriptografi kunci publik dalam sistem komunikasi digital. PKI mengatur proses pembuatan, distribusi, penyimpanan, dan pencabutan kunci publik serta sertifikat digital agar komunikasi antar pihak dapat berlangsung secara aman. Melalui PKI, pengguna dapat memverifikasi identitas pihak lain sebelum melakukan pertukaran informasi yang bersifat sensitif.

Dalam sistem PKI, Certificate Authority (CA) berperan sebagai pihak tepercaya yang memiliki kewenangan untuk menerbitkan sertifikat digital. CA melakukan proses verifikasi identitas terhadap individu, organisasi, atau sistem sebelum mengaitkan identitas tersebut dengan sepasang kunci kriptografi. Sertifikat digital yang diterbitkan oleh CA berfungsi sebagai bukti bahwa kunci publik tertentu benar-benar dimiliki oleh entitas yang sah.

Keberadaan PKI dan CA memungkinkan terwujudnya mekanisme keamanan seperti autentikasi, integritas data, dan non-repudiasi dalam komunikasi digital. Dengan adanya rantai kepercayaan yang dibangun oleh CA, pengguna dapat mempercayai kunci publik yang digunakan dalam proses enkripsi maupun verifikasi tanda tangan digital, sehingga risiko penyamaran identitas dan pemalsuan data dapat diminimalkan.

---

## 3. Alat dan Bahan
1. Buat folder berikut:  
   ```
   praktikum/week10-pki/
   ├─ src/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Gunakan Python 3.11 atau lebih baru.  
3. Install library tambahan jika diperlukan:  
   ```bash
   pip install cryptography pyopenssl
   ```
4. Materi rujukan: Stallings (2017), Bab 14.  
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

`from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")

Langkah 2 — Memverifikasi Sertifikat

Proses verifikasi sertifikat dilakukan dengan menggunakan public key milik Certificate Authority (CA) untuk memeriksa tanda tangan digital yang terdapat pada sertifikat tersebut. Jika hasil verifikasi berhasil, berarti sertifikat benar-benar diterbitkan oleh CA yang sah dan data di dalam sertifikat (seperti identitas pemilik dan public key) tidak mengalami perubahan sejak ditandatangani.

Peran CA sangat penting karena CA bertindak sebagai pihak tepercaya yang menjamin keaslian identitas pemilik sertifikat. CA melakukan proses validasi sebelum menerbitkan sertifikat dan menandatanganinya dengan private key milik CA. Selama public key CA dipercaya oleh sistem atau aplikasi (misalnya browser), maka sertifikat yang ditandatangani CA tersebut dianggap valid dan autentik.

Langkah 3 — Analisis PKI

Dalam praktik nyata, browser memverifikasi sertifikat HTTPS dengan memeriksa rantai kepercayaan (certificate chain), mulai dari sertifikat website hingga ke root certificate yang sudah tersimpan dan dipercaya di browser. Browser mengecek keabsahan tanda tangan digital, masa berlaku sertifikat, serta kecocokan nama domain. Jika seluruh proses valid, koneksi HTTPS akan dianggap aman.

Jika CA palsu atau CA yang diretas menerbitkan sertifikat, maka penyerang dapat melakukan serangan man-in-the-middle, yaitu menyamar sebagai website asli dan mencuri data pengguna. Oleh karena itu, browser dan sistem operasi secara berkala memperbarui daftar CA tepercaya dan dapat mencabut kepercayaan terhadap CA yang terbukti bermasalah.

PKI sangat penting dalam komunikasi aman karena menyediakan mekanisme enkripsi, autentikasi, dan integritas data secara bersamaan. Dalam konteks transaksi online, PKI memastikan bahwa pengguna benar-benar terhubung ke server yang sah dan data sensitif seperti kata sandi atau informasi pembayaran tidak dapat diubah maupun disadap oleh pihak yang tidak berwenang.

Kalau mau, aku bisa ringkaskan jadi versi laporan praktikum atau jawaban singkat ujian juga.

hilangkan kalimat cetak tebal

Berikut versi yang sama tanpa kalimat cetak tebal, tetap rapi dan naratif.

Langkah 2 — Memverifikasi Sertifikat

Proses verifikasi sertifikat dilakukan dengan menggunakan public key milik Certificate Authority (CA) untuk memeriksa tanda tangan digital yang terdapat pada sertifikat tersebut. Jika hasil verifikasi berhasil, berarti sertifikat benar-benar diterbitkan oleh CA yang sah dan data di dalam sertifikat, seperti identitas pemilik dan public key, tidak mengalami perubahan sejak ditandatangani.

Peran CA sangat penting karena CA bertindak sebagai pihak tepercaya yang menjamin keaslian identitas pemilik sertifikat. CA melakukan proses validasi sebelum menerbitkan sertifikat dan menandatanganinya dengan private key milik CA. Selama public key CA dipercaya oleh sistem atau aplikasi, misalnya browser, maka sertifikat yang ditandatangani CA tersebut dianggap valid dan autentik.

Langkah 3 — Analisis PKI

Dalam praktik nyata, browser memverifikasi sertifikat HTTPS dengan memeriksa rantai kepercayaan, mulai dari sertifikat website hingga ke root certificate yang sudah tersimpan dan dipercaya di browser. Browser mengecek keabsahan tanda tangan digital, masa berlaku sertifikat, serta kecocokan nama domain. Jika seluruh proses valid, koneksi HTTPS akan dianggap aman.

Jika CA palsu atau CA yang diretas menerbitkan sertifikat, maka penyerang dapat melakukan serangan man-in-the-middle, yaitu menyamar sebagai website asli dan mencuri data pengguna. Oleh karena itu, browser dan sistem operasi secara berkala memperbarui daftar CA tepercaya dan dapat mencabut kepercayaan terhadap CA yang terbukti bermasalah.

PKI sangat penting dalam komunikasi aman karena menyediakan mekanisme enkripsi, autentikasi, dan integritas data secara bersamaan. Dalam konteks transaksi online, PKI memastikan bahwa pengguna benar-benar terhubung ke server yang sah dan data sensitif seperti kata sandi atau informasi pembayaran tidak dapat diubah maupun disadap oleh pihak yang tidak berwenang.

---

## 6. Hasil dan Pembahasan
Berikut **hasil dan pembahasan** yang diringkas menjadi **2–3 paragraf** dan siap dipakai di laporan.

---

Berdasarkan hasil percobaan, program berhasil menghasilkan sebuah sertifikat digital bertipe self-signed yang ditandai dengan munculnya file cert.pem. Sertifikat ini memuat informasi identitas pemilik, public key, serta periode masa berlaku yang ditentukan. Proses penandatanganan sertifikat menggunakan algoritma kriptografi kunci publik RSA dengan fungsi hash SHA-256, yang menunjukkan bahwa sertifikat telah dilindungi oleh mekanisme tanda tangan digital.

Pada tahap pembahasan, sertifikat yang dihasilkan dapat diverifikasi menggunakan public key yang terdapat di dalam sertifikat tersebut karena bersifat self-signed. Hal ini membuktikan bahwa tanda tangan digital berfungsi untuk menjamin integritas data, di mana setiap perubahan pada isi sertifikat akan menyebabkan proses verifikasi gagal. Dengan demikian, keaslian dan keutuhan informasi dalam sertifikat dapat dipastikan selama kunci privat tidak disalahgunakan.

Secara konseptual, percobaan ini menggambarkan prinsip kerja Public Key Infrastructure (PKI), khususnya peran Certificate Authority (CA) dalam menerbitkan dan menandatangani sertifikat digital. Meskipun masih menggunakan CA sederhana, mekanisme ini serupa dengan sistem PKI di dunia nyata, seperti pada HTTPS, di mana kepercayaan terhadap sertifikat dibangun melalui CA tepercaya untuk menjamin keamanan komunikasi.

---

## 7. Jawaban Pertanyaan
1. Fungsi utama Certificate Authority (CA) adalah sebagai pihak tepercaya yang memverifikasi identitas pemilik sertifikat digital dan menandatangani sertifikat tersebut. Dengan tanda tangan CA, public key dalam sertifikat dapat dipercaya keasliannya sehingga pihak lain yakin bahwa kunci publik tersebut benar-benar milik entitas yang sah.

2. Self-signed certificate tidak cukup untuk sistem produksi karena tidak memiliki rantai kepercayaan (trust chain) ke CA tepercaya. Siapa pun dapat membuat sertifikat jenis ini, sehingga pengguna atau sistem tidak memiliki jaminan bahwa identitas pemilik sertifikat benar-benar valid. Akibatnya, self-signed certificate rentan disalahgunakan dan biasanya akan ditolak atau menimbulkan peringatan keamanan pada browser.

3. PKI mencegah serangan Man-in-the-Middle (MITM) dalam komunikasi TLS/HTTPS dengan memastikan bahwa sertifikat server telah diverifikasi oleh CA tepercaya. Browser memeriksa tanda tangan digital sertifikat dan mencocokkannya dengan root CA yang tersimpan. Jika sertifikat valid, public key server dapat dipercaya, sehingga penyerang tidak dapat menyisipkan kunci palsu tanpa terdeteksi.

---

## 8. Kesimpulan
Kesimpulannya, Certificate Authority (CA) memegang peran penting dalam membangun kepercayaan dengan memverifikasi identitas dan menerbitkan sertifikat digital yang sah. Penggunaan PKI memungkinkan komunikasi aman dengan menjamin keaslian, integritas, dan kerahasiaan data, terutama pada protokol TLS/HTTPS. Tanpa PKI dan CA yang tepercaya, sistem komunikasi modern akan sangat rentan terhadap serangan seperti man-in-the-middle.
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

    week10-cryptosystem: PKI)
```
