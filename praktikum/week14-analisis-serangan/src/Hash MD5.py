import hashlib

password = "admin123"
hash_md5 = hashlib.md5(password.encode()).hexdigest()

print("Password asli :", password)
print("Hash MD5      :", hash_md5)
