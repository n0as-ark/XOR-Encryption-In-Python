def xor_encrypt(plaintext: bytes, key: bytes) -> bytes:
    return bytes(
        byte ^ key[i % len(key)]
        for i, byte in enumerate(plaintext)
    )

xor_decrypt = xor_encrypt

key = b"SECRET"
message = b"Hello, World! This is a longer message."

ciphertext = xor_encrypt(message, key)
recovered = xor_decrypt(ciphertext, key)

print(recovered)    # b'Hello, World! This is a longer message.'


def hamming_distance(a: bytes, b: bytes) ->int:
    return sum(
        bin(x^y)        # XOR the two bytes to find differing bits 
        .count("1")     # count how many bits are different
        for x, y in zip(a,b)    # pair up corresponding bytes
    )

def guess_key_length(ciphertext: bytes, max_len: int = 40) -> int:
    # 40 is a practical upper bound - most repeating-key ciphers use keys
    # shorter than this, and longer keys need more ciphertext to measure reliably
    scores = []
    for klen in range(2, max_len +1):
        a = ciphertext[:klen]       # first chunk of guessed key length
        b = ciphertext[klen:klen*2] # second chunk right after
        score = hamming_distance(a, b) / klen # normalize by key length
        scores.append((score, klen))
    return min(scores)[1]       # key length with smallest distance is most likely correct

a = b"Hello"
b = b"World"
print(hamming_distance(a, b))  # 14

message = b"Hello, World! This is a longer message." * 20
ciphertext = xor_encrypt(message, b"SECRET")
print(guess_key_length(ciphertext))  # 39