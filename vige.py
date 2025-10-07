def _shift_char(c, k_shift):
    base = ord('A') if c.isupper() else ord('a')
    return chr((ord(c) - base + k_shift) % 26 + base)

def _key_shifts(key):
    return [ord(ch.upper()) - ord('A') for ch in key if ch.isalpha()]

def encrypt(plaintext, key):
    shifts = _key_shifts(key)
    if not shifts:
        return plaintext
    out = []
    ki = 0
    for ch in plaintext:
        if ch.isalpha():
            out.append(_shift_char(ch, shifts[ki % len(shifts)]))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

def decrypt(ciphertext, key):
    shifts = _key_shifts(key)
    if not shifts:
        return ciphertext
    out = []
    ki = 0
    for ch in ciphertext:
        if ch.isalpha():
            out.append(_shift_char(ch, -shifts[ki % len(shifts)]))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

if __name__ == "__main__":
    # 간단한 사용 예
    pt = "Hello, World!"
    k = "key"
    ct = encrypt(pt, k)
    print("plain:", pt)
    print("key:  ", k)
    print("enc:  ", ct)
    print("dec:  ", decrypt(ct, k))