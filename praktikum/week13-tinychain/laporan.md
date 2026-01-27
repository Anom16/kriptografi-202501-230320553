# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: TinyChain – Proof of Work (PoW) 
Nama: Anom Pangestu
NIM: 230320553
Kelas: 5DSRA

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan peran **hash function** dalam blockchain.  
2. Melakukan simulasi sederhana **Proof of Work (PoW)**.  
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.  
---

## 2. Dasar Teori
**Dasar Teori TinyChain – Proof of Work (PoW)**

TinyChain merupakan model blockchain sederhana yang digunakan untuk memahami konsep dasar teknologi blockchain, khususnya mekanisme konsensus **Proof of Work (PoW)**. Proof of Work adalah metode validasi blok di mana node atau miner harus menyelesaikan perhitungan kriptografi tertentu dengan menemukan nilai *nonce* yang menghasilkan hash sesuai tingkat kesulitan yang ditentukan. Mekanisme ini memastikan bahwa penambahan blok ke dalam blockchain memerlukan usaha komputasi, sehingga tidak dapat dilakukan secara sembarangan.

Dalam TinyChain, PoW berperan penting dalam menjaga **keamanan dan integritas data**. Setiap blok saling terhubung melalui hash blok sebelumnya, sehingga perubahan pada satu blok akan memengaruhi seluruh rantai blok. Proses PoW membuat manipulasi data menjadi sulit karena penyerang harus menghitung ulang Proof of Work pada seluruh blok berikutnya, yang membutuhkan sumber daya komputasi yang besar.

Meskipun efektif dalam meningkatkan keamanan, Proof of Work memiliki keterbatasan, terutama terkait efisiensi waktu dan penggunaan sumber daya. Oleh karena itu, TinyChain digunakan sebagai media pembelajaran untuk memahami prinsip kerja PoW secara konseptual tanpa kompleksitas dan konsumsi energi tinggi seperti pada blockchain skala besar, sehingga memudahkan pemahaman dasar teknologi blockchain.
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
   praktikum/week13-tinychain/
   ├─ src/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Gunakan Python 3.11 atau lebih baru.  
3. Materi rujukan:  
   - Stallings (2017), Bab 16.  
   - Stinson (2019), Bab 8.  

## 5. Source Code
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

### Langkah 2 — Membuat Blockchain

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))

---

## 6. Hasil dan Pembahasan
Proses mining pada blockchain membutuhkan waktu karena miner harus melakukan perhitungan hash secara berulang hingga memenuhi tingkat **difficulty** yang ditentukan. Semakin tinggi nilai *difficulty*, semakin banyak percobaan hash yang harus dilakukan, sehingga waktu yang dibutuhkan untuk menemukan blok yang valid menjadi lebih lama. Kondisi ini berdampak langsung pada keamanan blockchain, karena pembuatan blok tidak dapat dilakukan secara instan atau sembarangan, sehingga penyerang harus mengeluarkan usaha komputasi yang sangat besar untuk memalsukan atau mengubah data.

Untuk mengubah satu blok, penyerang tidak hanya perlu menghitung ulang proses mining pada blok tersebut, tetapi juga pada seluruh blok setelahnya. Hal ini membuat manipulasi data menjadi tidak realistis secara praktis karena membutuhkan waktu dan sumber daya yang sangat besar. Dengan demikian, peningkatan difficulty berfungsi sebagai mekanisme pengaman yang menjaga integritas dan keandalan blockchain meskipun dijalankan pada lingkungan yang tidak sepenuhnya saling percaya.

Hasil output mining menunjukkan bahwa mekanisme **Proof of Work (PoW)** telah berjalan dengan benar, di mana setiap blok hanya dianggap valid ketika hash yang dihasilkan diawali dengan sejumlah nol sesuai tingkat difficulty. Perbedaan hasil hash pada setiap proses mining menegaskan bahwa setiap blok memiliki hash yang unik dan saling terhubung, sehingga setiap perubahan data akan menyebabkan hash berubah dan proses mining harus diulang kembali, yang semakin memperkuat keamanan blockchain.

---

## 7. Jawaban Pertanyaan
1. Fungsi hash penting dalam blockchain karena menjamin integritas data, menghubungkan setiap blok secara aman, dan memungkinkan deteksi perubahan data sekecil apa pun pada blockchain.

2. Proof of Work mencegah double spending dengan memastikan setiap transaksi hanya dapat dicatat satu kali dalam blok yang telah divalidasi melalui proses komputasi yang sulit dan disepakati sebelum ditambahkan ke blockchain.

3. Kelemahan PoW dalam efisiensi energi adalah membutuhkan daya komputasi dan konsumsi listrik yang sangat besar karena proses mining dilakukan secara berulang hingga menemukan hash yang sesuai.

---

## 8. Kesimpulan
**Kesimpulan**

Teknologi blockchain dengan mekanisme konsensus **Proof of Work (PoW)** berperan penting dalam menjaga keamanan dan integritas data. Fungsi hash kriptografi memastikan setiap blok memiliki identitas unik dan saling terhubung, sehingga setiap perubahan data dapat terdeteksi. Proses mining yang melibatkan perhitungan hash berulang dengan tingkat *difficulty* tertentu membuktikan bahwa penambahan blok ke dalam blockchain memerlukan usaha komputasi yang nyata dan tidak dapat dilakukan secara sembarangan.

Hasil implementasi dan pengujian menunjukkan bahwa semakin tinggi nilai *difficulty*, semakin lama waktu yang dibutuhkan untuk melakukan mining, namun hal tersebut justru memperkuat keamanan sistem. Output mining memperlihatkan bahwa setiap blok memiliki hash yang unik dan valid sesuai ketentuan Proof of Work serta terhubung dengan blok sebelumnya. Dengan demikian, mekanisme PoW efektif dalam mencegah manipulasi data dan menjadikan blockchain sebagai sistem pencatatan yang aman, andal, dan terpercaya.

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

    week13-cryptosystem )
```
