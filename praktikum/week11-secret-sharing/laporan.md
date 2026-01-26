# Laporan Praktikum Kriptografi
Minggu ke-: 11
Topik: Secret Sharing (Shamir’s Secret Sharing)
Nama: Anom Pangestu
NIM: 230320553
Kelas: 5DSRA

---

## 1. Tujuan
1. Menjelaskan konsep **Shamir Secret Sharing** (SSS).  
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.  
3. Menganalisis keamanan skema distribusi rahasia.  
---

## 2. Dasar Teori
Shamir’s Secret Sharing merupakan skema kriptografi yang digunakan untuk membagi sebuah rahasia menjadi beberapa bagian (share) sehingga rahasia tersebut tidak dapat diketahui hanya dari satu bagian saja. Dalam skema ini, rahasia awal dipecah menjadi n buah share dan kemudian didistribusikan kepada beberapa pihak. Rahasia baru dapat direkonstruksi kembali apabila sedikitnya t share (threshold) digabungkan, sedangkan jika jumlah share yang dimiliki kurang dari t, maka tidak diperoleh informasi apa pun mengenai rahasia tersebut.

Dasar teori Shamir’s Secret Sharing bertumpu pada konsep interpolasi polinomial dalam matematika. Rahasia direpresentasikan sebagai konstanta dari sebuah polinomial berderajat t−1, kemudian nilai polinomial tersebut dihitung pada beberapa titik berbeda untuk menghasilkan share. Sifat utama dari polinomial adalah bahwa diperlukan minimal t titik berbeda untuk merekonstruksi polinomial secara unik, sehingga menjamin bahwa kurang dari t share tidak cukup untuk mengungkap rahasia.

Skema ini banyak digunakan dalam sistem yang membutuhkan tingkat keamanan dan keandalan tinggi, seperti pengelolaan kunci kriptografi, sistem backup aman, dan manajemen akses terdistribusi. Dengan membagi rahasia ke beberapa pihak, risiko kebocoran akibat satu titik kegagalan dapat dikurangi, sekaligus memastikan bahwa kolaborasi sejumlah pihak diperlukan untuk mengakses informasi sensitif.
---

## 3. Alat dan Bahan
1. Buat folder berikut:  
   ```
   praktikum/week11-secret-sharing/
   ├─ src/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Gunakan Python 3.11 atau lebih baru.  
3. Install library tambahan bila perlu:  
   ```bash
   pip install secretsharing
   ```  
   atau gunakan implementasi mandiri dengan operasi aritmetika modular.  
4. Materi rujukan: Stinson (2019), Bab 6. 
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code

```python
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)
```

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
