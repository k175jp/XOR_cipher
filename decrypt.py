import pwn

# png signature
signature = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"

# read xor flag
with open("flag.png", "rb") as f:
    encrypt = f.read()

# key = b'THISISXO'
key = pwn.xor(encrypt, signature)[0:len(signature)]

# key is less than 10 letters, so you guessed it.
key = key + b"R"

# decrypt flag
flag = pwn.xor(encrypt, key)

# write flag
with open("decrypt_flag.png", "wb") as f:
    f.write(flag)
