import pwn

signature = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A" # png signature

with open("flag.png", "rb") as f:
    encrypt = f.read()

# key = b'THISISXO'
key = pwn.xor(encrypt, signature)[0:8]

# key is less than 10 letters
key = key + b"R"


flag = pwn.xor(encrypt, key)

with open("decrypt_flag.png", "wb") as f:
    f.write(flag)
