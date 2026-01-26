from shamir_mnemonic import generate_mnemonics, combine_mnemonics

# Rahasia dalam bentuk string (akan dikonversi otomatis)
secret = "rahasia_sangat_penting"

# Parameter:
# group_threshold = 1  -> hanya 1 grup diperlukan
# groups = [(3, 5)]    -> threshold 3 dari 5 share
mnemonics = generate_mnemonics(
    group_threshold=1,
    groups=[(3, 5)],
    master_secret=secret.encode()
)

print("Shares:")
for share in mnemonics[0]:
    print(share)

# Rekonstruksi rahasia (pakai 3 share pertama)
recovered = combine_mnemonics(mnemonics[0][:3])

print("Secret berhasil direkonstruksi:", recovered.decode())
