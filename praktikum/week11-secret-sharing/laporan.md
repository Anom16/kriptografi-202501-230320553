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
Hasil percobaan menunjukkan bahwa skema Shamir’s Secret Sharing mampu membagi sebuah rahasia menjadi beberapa bagian (share) tanpa mengungkapkan nilai rahasia itu sendiri. Setiap share yang dihasilkan berdiri sendiri dan tidak memberikan informasi berarti apabila dilihat secara terpisah. Hal ini membuktikan bahwa mekanisme pembagian rahasia bekerja sesuai dengan prinsip keamanan, di mana tidak ada satu pihak pun yang memiliki akses penuh terhadap rahasia.

Pada tahap rekonstruksi, rahasia hanya dapat dikembalikan ketika jumlah share yang digunakan memenuhi nilai threshold yang telah ditentukan. Ketika share yang digabungkan kurang dari threshold, proses rekonstruksi gagal dan rahasia tidak dapat diperoleh. Sebaliknya, saat jumlah share mencukupi, rahasia berhasil direkonstruksi secara utuh, yang menunjukkan bahwa skema ini menjamin kontrol akses berbasis jumlah pihak yang berwenang.

Pembahasan ini menegaskan bahwa Shamir’s Secret Sharing efektif dalam mengurangi risiko kebocoran dan single point of failure. Dengan membagi rahasia ke beberapa pihak, sistem menjadi lebih aman dan andal, terutama untuk pengelolaan kunci kriptografi dan informasi sensitif yang membutuhkan kolaborasi serta tingkat kepercayaan tinggi antar pihak.

---

## 7. Jawaban Pertanyaan
1. Keuntungan utama Shamir Secret Sharing adalah rahasia tidak pernah disimpan atau dibagikan dalam bentuk utuh kepada satu pihak. Berbeda dengan membagikan salinan kunci secara langsung yang berisiko bocor jika satu pihak disusupi, SSS memastikan bahwa satu atau beberapa bagian saja tidak cukup untuk mengetahui rahasia, sehingga tingkat keamanannya jauh lebih tinggi.

2. Threshold (k) berperan sebagai batas minimum jumlah share yang harus digabungkan untuk merekonstruksi rahasia. Selama jumlah share yang dimiliki kurang dari k, rahasia tetap aman dan tidak dapat ditebak, sehingga threshold menjadi mekanisme utama yang mengontrol keseimbangan antara keamanan dan ketersediaan akses.

3. Contoh skenario nyata penggunaan SSS adalah penyimpanan kunci utama server perusahaan, di mana kunci dibagi kepada beberapa manajer. Kunci tersebut hanya dapat digunakan jika minimal sejumlah manajer tertentu hadir dan menyetujui, sehingga mencegah penyalahgunaan oleh satu orang dan mengurangi risiko kehilangan akses akibat satu titik kegagalan.

---

## 8. Kesimpulan
hamir’s Secret Sharing merupakan metode yang efektif untuk melindungi rahasia dengan cara membaginya ke dalam beberapa bagian sehingga tidak ada satu pihak pun yang memegang rahasia secara utuh. Penggunaan threshold memastikan bahwa hanya pihak yang berwenang dan memenuhi jumlah minimum tertentu yang dapat merekonstruksi rahasia. Dengan demikian, skema ini meningkatkan keamanan sekaligus keandalan dalam pengelolaan informasi sensitif.

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

    week11-cryptosystem: secret sharing )
```
