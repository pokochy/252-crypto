def _shift_char(c, shift):
    if c.isupper():
        base = ord('A')
    elif c.islower():
        base = ord('a')
    else:
        return c
    return chr((ord(c) - base + shift) % 26 + base)

def encrypt(plaintext, shift):
    s = shift % 26
    return ''.join(_shift_char(ch, s) for ch in plaintext)

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

if __name__ == "__main__":
    pt = "Hello, World!"
    k = 3
    ct = encrypt(pt, k)
    print("plain:", pt)
    print("shift:", k)
    print("enc:  ", ct)
    print("dec:  ", decrypt(ct, k))