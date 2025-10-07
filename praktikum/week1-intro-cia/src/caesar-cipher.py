
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

# --- Eksekusi utama ---
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
