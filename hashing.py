# hashing is a one way function. Same input --> same output.

import hashlib

password = "He||0"

data = password.encode("utf-8")

digest = hashlib.md5(data).hexdigest()


print(f"Password: {password}, \n Hash: {digest}")

x = ["He||0","yes","never!","monkey1000??", "1eX1st"]

#x = {"He||0","yes","never!","monkey1000??", "1eX1st"}



for i in x:
    print(f"Password hash of {i}: {hashlib.sha256(i.encode("utf-8")).hexdigest()}\n")