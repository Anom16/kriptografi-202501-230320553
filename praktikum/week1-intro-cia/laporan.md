# Laporan Praktikum Kriptografi
Minggu ke-: 1 
Topik: CIA Intro 
Nama: Anom Pangestu
NIM: 230320553
Kelas: 5DSRA

---

## 1. Tujuan
1. Menjelaskan **sejarah dan evolusi kriptografi** dari masa klasik hingga modern.  
2. Menyebutkan **prinsip Confidentiality, Integrity, Availability (CIA)** dengan benar.  
3. Menyimpulkan **peran kriptografi** dalam sistem keamanan informasi modern.  
4. Menyiapkan repositori GitHub sebagai media kerja praktikum.  

## 2. Dasar Teori
Cipher klasik adalah bentuk awal dari kriptografi yang berfokus pada penyandian pesan menggunakan manipulasi huruf atau simbol. Prinsip dasarnya adalah mengubah teks asli (*plaintext*) menjadi teks sandi (*ciphertext*) dengan mengikuti aturan tertentu agar isi pesan tidak dapat dipahami oleh pihak yang tidak berwenang. Dua pendekatan utama yang digunakan dalam cipher klasik adalah substitusi, yaitu mengganti setiap huruf dengan huruf lain, dan transposisi, yaitu mengubah urutan huruf tanpa mengubah bentuknya.

Contoh paling terkenal dari cipher klasik adalah Caesar Cipher, yang menggeser setiap huruf sejumlah posisi tertentu dalam alfabet, serta Vigenère Cipher, yang menggunakan kata kunci untuk menciptakan pola substitusi yang lebih kompleks. Pada masa sebelum komputer, metode ini cukup efektif karena analisis pesan harus dilakukan secara manual. Namun, seiring berkembangnya kemampuan komputasi, cipher klasik menjadi mudah dipecahkan melalui analisis frekuensi dan brute force, sehingga tingkat keamanannya dianggap rendah di era modern.

Meskipun sudah usang secara praktis, cipher klasik memiliki nilai penting dalam sejarah kriptografi. Ia menjadi dasar pemahaman tentang konsep enkripsi, dekripsi, kunci, dan kerahasiaan informasi, yang kemudian dikembangkan lebih lanjut dalam kriptografi modern. Dengan kata lain, cipher klasik adalah pondasi intelektual yang menandai peralihan dari teknik penyamaran sederhana menuju sistem keamanan berbasis matematika yang kompleks.


---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code 
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )
 
---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week1-intro-cia/src/`.
2. membuat kode program.
3. Menjalankan program dengan perintah `caesar_cipher.py`.

---

## 5. Source Code


```python

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # hanya huruf yang dienkripsi
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


print("=== Program Caesar Cipher ===")
pilihan = input("Pilih mode (E untuk Enkripsi / D untuk Dekripsi): ").upper()
pesan = input("Masukkan teks: ")
kunci = int(input("Masukkan kunci (angka): "))

if pilihan == "E":
    hasil = encrypt(pesan, kunci)
    print("\nHasil enkripsi:", hasil)
elif pilihan == "D":
    hasil = decrypt(pesan, kunci)
    print("\nHasil dekripsi:", hasil)
else:
    print("\nPilihan tidak valid. Gunakan E atau D.")




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
- Pertanyaan 1: Whitfield Diffie dan Martin Hellman
- Pertanyaan 2: Algoritma kunci publik yang populer digunakan saat ini antara lain RSA (Rivest–Shamir–Adleman), ECC (Elliptic Curve Cryptography), dan Diffie–Hellman Key Exchange.
-Pertanyaan 3 : Kriptografi klasik menggunakan teknik sederhana seperti substitusi dan transposisi huruf, dengan keamanan bergantung pada kerahasiaan algoritma dan kunci yang relatif lemah. Sebaliknya, kriptografi modern berbasis matematika dan teori komputasi, menggunakan operasi kompleks pada bit atau bilangan besar, serta bergantung pada kesulitan masalah matematis (seperti faktorisasi atau logaritma diskrit) untuk menjamin keamanan.)

## 8. Kesimpulan
(Hasil eksekusi program menunjukkan bahwa proses enkripsi dan dekripsi pada algoritma Caesar Cipher berjalan dengan benar. Saat teks asli “Anom Pangestu” dienkripsi menggunakan kunci 16, program menghasilkan ciphertext “Qdec Fqdwujjk”. Ini menunjukkan bahwa setiap huruf dalam plaintext digeser sejauh 16 posisi ke kanan dalam alfabet. Ketika ciphertext tersebut didekripsi kembali dengan kunci yang sama, hasilnya kembali menjadi “Anom Pangestu”. Hal ini membuktikan bahwa mekanisme simetris pada Caesar Cipher berfungsi sebagaimana mestinya, di mana proses enkripsi dan dekripsi saling membalikkan satu sama lain.

Secara teoritis, Caesar Cipher merupakan bentuk cipher substitusi paling sederhana yang hanya bergantung pada satu kunci pergeseran. Keberhasilan dekripsi dengan hasil yang identik membuktikan bahwa implementasi program telah mengikuti prinsip dasar algoritma ini, yaitu pergeseran huruf secara tetap berdasarkan nilai kunci. Namun, dari sisi keamanan, Caesar Cipher tergolong sangat lemah karena hanya memiliki 26 kemungkinan kunci (untuk alfabet Latin), sehingga pesan mudah dipecahkan melalui brute force atau analisis frekuensi huruf.

Dengan demikian, hasil percobaan ini memperlihatkan pemahaman mendasar tentang konsep enkripsi dan dekripsi dalam kriptografi klasik. Walaupun sederhana dan tidak lagi relevan untuk pengamanan data modern, Caesar Cipher tetap penting sebagai sarana pembelajaran untuk memahami prinsip dasar pengubahan teks agar tidak terbaca oleh pihak yang tidak berwenang. )

---

## 9. Daftar Pustaka
(Stallings, W. (2017). Cryptography and network security: Principles and practice (7th ed.). Pearson Education.
Singh, S. (1999). The code book: The science of secrecy from ancient Egypt to quantum cryptography. Anchor Books.
Kahn, D. (1996). The codebreakers: The comprehensive history of secret communication from ancient times to the internet. Scribner.
Schneier, B. (1996). Applied cryptography: Protocols, algorithms, and source code in C (2nd ed.). Wiley.
Alani, M. M. (2016). Guide to cryptography. Springer. )

---

## 10. Commit Log
( Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit introcia1
Author: Nama Mahasiswa <anompangestu16@gmail.com>
Date:   2025-10-07

    week1-intro-cia )
```
