def _build_maps(key):
    k = ''.join(ch.upper() for ch in key if ch.isalpha())
    if len(k) != 26 or len(set(k)) != 26:
        raise ValueError("key must contain 26 unique letters")
    plain = [chr(ord('A') + i) for i in range(26)]
    enc_map = {p: c for p, c in zip(plain, k)}
    dec_map = {c: p for p, c in zip(plain, k)}
    return enc_map, dec_map

def encrypt(plaintext, key):
    enc_map, _ = _build_maps(key)
    out = []
    for ch in plaintext:
        if ch.isupper():
            out.append(enc_map.get(ch, ch))
        elif ch.islower():
            out.append(enc_map.get(ch.upper(), ch).lower())
        else:
            out.append(ch)
    return ''.join(out)

def decrypt(ciphertext, key):
    _, dec_map = _build_maps(key)
    out = []
    for ch in ciphertext:
        if ch.isupper():
            out.append(dec_map.get(ch, ch))
        elif ch.islower():
            out.append(dec_map.get(ch.upper(), ch).lower())
        else:
            out.append(ch)
    return ''.join(out)

if __name__ == "__main__":
    # 사용 예
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"  # 26글자 치환 키
    pt = "Hello, World!"
    ct = encrypt(pt, key)
    print("plain:", pt)
    print("key:  ", key)
    print("enc:  ", ct)
    print("dec:  ", decrypt(ct, key))