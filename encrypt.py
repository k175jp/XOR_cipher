import pwn

with open('flag.png', 'rb') as f:
    flag = f.read()

xor_key = 'xxxxxxxxxx' # I forgot about it... But it was less than 10 letters.
crypted_flag = pwn.xor(flag, xor_key)

with open('flag.png', 'wb') as f:
    f.write(crypted_flag)
