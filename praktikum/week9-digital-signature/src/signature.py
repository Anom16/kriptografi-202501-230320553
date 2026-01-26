from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# =========================
# Langkah 1 — Generate Key dan Buat Tanda Tangan
# =========================

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan asli
message = b"Hello, ini pesan penting."

# Hash pesan
hash_message = SHA256.new(message)

# Buat tanda tangan menggunakan private key
signature = pkcs1_15.new(private_key).sign(hash_message)

print("Signature:", signature.hex())

# =========================
# Langkah 2 — Verifikasi Tanda Tangan
# =========================

try:
    pkcs1_15.new(public_key).verify(hash_message, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# =========================
# Langkah 3 — Uji Modifikasi Pesan
# =========================

# Pesan yang dimodifikasi
fake_message = b"Hello, ini pesan palsu."

# Hash pesan palsu
hash_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(hash_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
