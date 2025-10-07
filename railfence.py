def encrypt(plaintext, rails):
    if rails <= 1:
        return plaintext
    pattern = []
    r = 0
    step = 1
    for _ in plaintext:
        pattern.append(r)
        r += step
        if r == 0 or r == rails - 1:
            step = -step
    rows = [''] * rails
    for p, ch in zip(pattern, plaintext):
        rows[p] += ch
    return ''.join(rows)

def decrypt(ciphertext, rails):
    if rails <= 1:
        return ciphertext
    n = len(ciphertext)
    pattern = []
    r = 0
    step = 1
    for _ in range(n):
        pattern.append(r)
        r += step
        if r == 0 or r == rails - 1:
            step = -step
    counts = [pattern.count(i) for i in range(rails)]
    parts = []
    idx = 0
    for c in counts:
        parts.append(list(ciphertext[idx:idx+c]))
        idx += c
    out = []
    for p in pattern:
        out.append(parts[p].pop(0))
    return ''.join(out)

if __name__ == "__main__":
    pt = "WEAREDISCOVEREDFLEEATONCE"
    r = 3
    ct = encrypt(pt, r)
    print("plain:", pt)
    print("rails:", r)
    print("enc:  ", ct)
    print("dec:  ", decrypt(ct, r))