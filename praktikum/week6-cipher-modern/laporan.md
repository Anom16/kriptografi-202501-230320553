# Laporan Praktikum Kriptografi Minggu ke-6

**Topik:** Cipher Modern (DES, AES, RSA)

**Nama:** Anom Pangestu
**NIM:** 230320553
**Kelas:** 5DSRA

---

## 1. Tujuan

1. Mengimplementasikan algoritma DES untuk enkripsi–dekripsi blok data sederhana (simulasi).
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan serta mengimplementasikan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori

DES (Data Encryption Standard) adalah algoritma kriptografi simetris berbasis blok 64 bit dengan panjang kunci efektif 56 bit. Walaupun historis penting, DES saat ini tidak lagi dianggap aman karena ukuran kuncinya kecil dan rentan terhadap brute force. Oleh karena itu, implementasi DES pada praktikum ini bersifat simulasi untuk memahami konsep cipher blok.

AES (Advanced Encryption Standard) merupakan algoritma simetris modern yang menggantikan DES. AES menggunakan ukuran blok 128 bit dengan panjang kunci 128, 192, atau 256 bit. Keamanan AES bergantung pada struktur substitusi–permutasi yang kuat dan efisiensi tinggi, sehingga luas digunakan pada sistem keamanan modern.

RSA adalah algoritma kriptografi kunci publik (asimetris) yang keamanannya bertumpu pada kesulitan faktorisasi bilangan prima besar. RSA menggunakan sepasang kunci, yaitu kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Algoritma ini banyak digunakan untuk pertukaran kunci dan tanda tangan digital.

---

## 3. Alat dan Bahan

* Python 3.11
* Visual Studio Code
* Git dan akun GitHub

---

## 4. Langkah Percobaan

1. Membuat struktur folder `praktikum/week6-cipher-modern/` beserta subfolder `src`, `screenshots`, dan file `laporan.md`.
2. Menginstal library tambahan dengan perintah `pip install pycryptodome`.
3. Membuat file `aes.py`, `rsa.py`, dan `des.py` pada folder `src`.
4. Menyalin dan menyesuaikan kode program AES, RSA, dan DES sesuai panduan praktikum.
5. Menjalankan program menggunakan perintah `python nama_file.py`.
6. Mengambil screenshot hasil enkripsi dan dekripsi.
7. Melakukan commit ke GitHub dengan pesan `week6-cipher-modern`.

---

## 5. Source Code

### AES-128 (aes.py)

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print(decrypted.decode())
```

### RSA (rsa.py)

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)

decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print(decrypted.decode())
```

### DES (des.py – opsional)

```python
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)
plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print(decrypted)
```

---

## 6. Hasil dan Pembahasan

Program AES, RSA, dan DES berhasil dijalankan dan menghasilkan keluaran berupa plaintext yang sama setelah proses dekripsi. Hal ini menunjukkan bahwa proses enkripsi–dekripsi berjalan dengan benar.

DES berhasil mengenkripsi blok data 8 byte, namun digunakan dalam mode ECB yang memiliki kelemahan keamanan. AES menggunakan mode EAX yang lebih aman karena menyediakan autentikasi data. RSA berhasil mengenkripsi pesan pendek menggunakan kunci publik dan mendekripsinya dengan kunci privat.

![Hasil Eksekusi](screenshots/hasil.png)

---

## 7. Jawaban Pertanyaan

**1. Perbedaan DES, AES, dan RSA:**
DES dan AES adalah algoritma simetris yang menggunakan satu kunci yang sama untuk enkripsi dan dekripsi, sedangkan RSA adalah algoritma asimetris yang menggunakan pasangan kunci publik dan privat.

**2. Alasan AES lebih banyak digunakan dibanding DES:**
AES memiliki ukuran kunci yang lebih besar dan struktur algoritma yang lebih kuat sehingga jauh lebih aman dibanding DES.

**3. RSA sebagai algoritma asimetris:**
RSA disebut asimetris karena menggunakan dua kunci berbeda. Proses pembangkitan kunci melibatkan pemilihan dua bilangan prima besar dan perhitungan modulus serta eksponen publik dan privat.

---

## 8. Kesimpulan

Berdasarkan praktikum yang dilakukan, AES dan RSA terbukti merupakan algoritma kriptografi modern yang aman dan relevan digunakan saat ini. DES hanya layak digunakan sebagai bahan pembelajaran karena keterbatasan keamanannya.

---

## 9. Daftar Pustaka

* Stallings, W. *Cryptography and Network Security*.
* Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.

---

## 10. Commit Log

```
commit week 6
Author: Anom Pangestu
Message: week6-cipher-modern
```
