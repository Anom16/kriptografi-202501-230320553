# Laporan Praktikum Kriptografi

Minggu ke-: 5
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: [Nama Mahasiswa]
NIM: [NIM Mahasiswa]
Kelas: [Kelas]

---

## 1. Tujuan

Praktikum ini bertujuan untuk memahami dan mengimplementasikan algoritma kriptografi klasik, khususnya Caesar Cipher, Vigenère Cipher, dan cipher transposisi sederhana. Selain itu, praktikum ini bertujuan mengevaluasi kelemahan keamanan cipher klasik melalui pengujian enkripsi dan dekripsi serta analisis konseptual.

---

## 2. Dasar Teori

Cipher klasik adalah metode kriptografi awal yang digunakan untuk menyamarkan pesan dengan teknik substitusi atau transposisi karakter. Keamanan cipher klasik umumnya bergantung pada kerahasiaan kunci dan kesederhanaan transformasi matematis, seperti pergeseran alfabet (Caesar Cipher) atau penambahan kunci berulang (Vigenère Cipher).

Caesar Cipher merupakan cipher substitusi monoalfabetik yang menggunakan pergeseran tetap pada alfabet. Vigenère Cipher adalah pengembangan cipher substitusi polialfabetik yang menggunakan kata kunci untuk menentukan besar pergeseran setiap karakter. Sementara itu, cipher transposisi tidak mengubah karakter, tetapi mengubah posisi karakter dalam plaintext berdasarkan kunci tertentu.

---

## 3. Alat dan Bahan

* Python 3.11
* Visual Studio Code
* Git dan GitHub
* Sistem operasi Windows

---

## 4. Langkah Percobaan

1. Membuat struktur folder `praktikum/week5-cipher-klasik/` sesuai instruksi modul.
2. Membuat file program Python untuk Caesar Cipher, Vigenère Cipher, dan Transposisi.
3. Menuliskan kode program berdasarkan panduan praktikum.
4. Menjalankan masing-masing program menggunakan perintah `python nama_file.py`.
5. Mengambil screenshot hasil enkripsi dan dekripsi.
6. Menyusun laporan praktikum dalam file `laporan.md`.

---

## 5. Source Code

### Caesar Cipher

```python
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)
```

### Vigenère Cipher

```python
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)
```

---

## 6. Hasil dan Pembahasan

Hasil pengujian menunjukkan bahwa seluruh algoritma berhasil melakukan proses enkripsi dan dekripsi dengan benar. Pesan yang telah dienkripsi dapat dikembalikan ke bentuk plaintext semula menggunakan kunci yang sama.

Cipher Caesar menghasilkan ciphertext dengan pola pergeseran yang mudah dikenali. Vigenère Cipher menghasilkan ciphertext yang lebih bervariasi karena penggunaan kunci berulang. Cipher transposisi mengubah urutan karakter tanpa mengubah karakter itu sendiri.

Screenshot hasil eksekusi program dilampirkan pada folder `screenshots/`.

---

## 7. Jawaban Pertanyaan

**1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?**
Caesar Cipher memiliki ruang kunci yang sangat kecil (hanya 25 kemungkinan), sehingga mudah dipecahkan dengan brute force. Vigenère Cipher lebih kuat, tetapi tetap rentan jika panjang kunci pendek atau berulang, sehingga dapat diserang menggunakan analisis Kasiski atau Friedman test.

**2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?**
Karena cipher klasik mempertahankan karakteristik statistik bahasa asli. Frekuensi kemunculan huruf pada ciphertext masih mencerminkan frekuensi bahasa plaintext, sehingga pola ini dapat dimanfaatkan untuk memecahkan kunci.

**3. Bandingkan cipher substitusi dan transposisi.**
Cipher substitusi mengubah karakter plaintext menjadi karakter lain, sedangkan cipher transposisi hanya mengubah posisi karakter. Substitusi rentan terhadap analisis frekuensi, sementara transposisi rentan terhadap analisis pola. Keduanya tidak cukup aman jika digunakan secara tunggal.

---

## 8. Kesimpulan

Cipher klasik dapat diimplementasikan dengan mudah dan efektif untuk tujuan pembelajaran. Namun, dari sisi keamanan, cipher klasik memiliki banyak kelemahan sehingga tidak layak digunakan untuk pengamanan data modern.

---

## 9. Daftar Pustaka

* Stallings, W. *Cryptography and Network Security: Principles and Practice*.
* Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.

---

## 10. Commit Log

```
commit abc12345
Author: Anom Pangestu (ansman13579@gmail.com)
Date:   2025-11-11

    week5-cipher-klasik
```
