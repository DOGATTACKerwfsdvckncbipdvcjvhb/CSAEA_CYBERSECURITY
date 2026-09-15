import hashlib
import os

passthing= "monkey1000?!"

password = passthing.encode("utf-8")

#1. Regular hash, no salt. For two users, same password --> identical hashes

print("User passwords hashed")
hash_a = hashlib.sha256(password).hexdigest()


hash_b = hashlib.sha256(password).hexdigest()

print("No salt:  ")
print(f"User A: {hash_a}\nUser B: {hash_b}")

# Add salt. Each user will get their own random SALT.

salt_a = os.urandom(16).hex()

salt_b = os.urandom(16).hex()

print("Salt A by itself:  ",salt_a)

print("Salt B by itself:  ",salt_b)

shash_a = salt_a+hashlib.sha256(password).hexdigest()

shash_b = salt_b+hashlib.sha256(password).hexdigest()

print("\n\n\n\nUser passwords hashed with salt")
print(f"User A: {shash_a}\nUser B: {shash_b}")