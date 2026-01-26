# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Digital Signature (RSA/DSA)
Nama: Anom Pangestu 
NIM: 230320553
Kelas: 5DSRA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.  
2. Memverifikasi keaslian tanda tangan digital.  
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.  
---

## 2. Dasar Teori
Tanda tangan digital merupakan teknik kriptografi yang digunakan untuk menjamin keaslian, keutuhan, dan keabsahan suatu pesan atau dokumen digital. Mekanisme ini memungkinkan penerima untuk memverifikasi bahwa pesan benar-benar berasal dari pengirim yang sah dan tidak mengalami perubahan selama proses pengiriman. Berbeda dengan enkripsi yang bertujuan menjaga kerahasiaan data, tanda tangan digital berfokus pada autentikasi identitas pengirim dan integritas informasi.

Pada skema RSA, tanda tangan digital dibuat dengan memanfaatkan pasangan kunci privat dan kunci publik. Pengirim menghasilkan tanda tangan dengan mengenkripsi nilai hash dari pesan menggunakan kunci privatnya. Penerima kemudian melakukan verifikasi dengan kunci publik pengirim untuk memastikan bahwa tanda tangan tersebut valid. Keamanan RSA bergantung pada kesulitan memfaktorkan bilangan besar, sehingga pemalsuan tanda tangan menjadi tidak praktis secara komputasional.

Sementara itu, Digital Signature Algorithm (DSA) didasarkan pada masalah logaritma diskret. Proses penandatanganan dilakukan menggunakan kunci privat dan bilangan acak tertentu, sedangkan verifikasi dilakukan dengan kunci publik. Keamanan DSA sangat bergantung pada kerahasiaan nilai acak yang digunakan dalam proses penandatanganan. Baik RSA maupun DSA memberikan jaminan non-repudiasi, sehingga pengirim tidak dapat menyangkal keabsahan tanda tangan yang telah dibuat.
---

## 3. Alat dan Bahan
1. Buat folder berikut:  
   ```
   praktikum/week9-digital-signature/
   ├─ src/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Gunakan Python 3.11 atau lebih baru.  
3. Install library tambahan:  
   ```bash
   pip install pycryptodome
   ```
4. Materi rujukan: Stinson (2019), Bab 5.  

---

## 4. Langkah Percobaan
Panduan Langkah demi Langkah

1. Generate Key dan Buat Tanda Tangan
2. Verifikasi Tanda Tangan
3. Uji Modifikasi Pesan
---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

## Panduan Langkah demi Langkah

### Langkah 1 — Generate Key dan Buat Tanda Tangan
```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
```

---

### Langkah 2 — Verifikasi Tanda Tangan
```python
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
```

---

### Langkah 3 — Uji Modifikasi Pesan
```python
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```

---

## 6. Hasil dan Pembahasan
Berdasarkan hasil eksekusi program tanda tangan digital RSA, diperoleh dua keluaran utama, yaitu *“Verifikasi berhasil: tanda tangan valid”* dan *“Verifikasi gagal: tanda tangan tidak cocok dengan pesan”*. Hasil ini menunjukkan bahwa mekanisme tanda tangan digital bekerja sesuai dengan teori yang mendasarinya.

Pada pengujian pertama, pesan asli yang ditandatangani menggunakan kunci privat berhasil diverifikasi menggunakan kunci publik. Hal ini membuktikan bahwa tanda tangan yang dihasilkan valid dan pesan benar-benar berasal dari pihak yang memiliki kunci privat tersebut. Selain itu, keberhasilan verifikasi juga menandakan bahwa isi pesan tidak mengalami perubahan sejak proses penandatanganan dilakukan.

Pada pengujian kedua, pesan dimodifikasi setelah tanda tangan dibuat. Meskipun tanda tangan yang digunakan sama, proses verifikasi gagal karena nilai hash dari pesan yang telah diubah tidak lagi sesuai dengan hash pesan asli yang ditandatangani. Kegagalan ini menunjukkan bahwa tanda tangan digital mampu mendeteksi perubahan sekecil apa pun pada pesan, sehingga menjamin integritas data. Dengan demikian, hasil simulasi ini membuktikan bahwa tanda tangan digital RSA efektif dalam memastikan keaslian pengirim dan keutuhan pesan.

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
Berdasarkan hasil percobaan, tanda tangan digital RSA berhasil diverifikasi ketika pesan tidak mengalami perubahan, yang menunjukkan bahwa pesan berasal dari pengirim yang sah dan tetap utuh. Sebaliknya, saat pesan dimodifikasi, proses verifikasi gagal karena tanda tangan tidak lagi sesuai dengan isi pesan. Hal ini membuktikan bahwa tanda tangan digital efektif dalam menjamin keaslian dan integritas pesan.

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
commit week 9
Author: anom pangestu
Date:   2026-01

    week9-cryptosystem: signature  )
```
