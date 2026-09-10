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
    for klen in range(2, min(max_len +1, len(ciphertext) // 2 + 1)):    # cap at half ciphertext length
        distances = []
        for j in range(min(4, len(ciphertext) // klen - 1)):    # average multiple pairs
            a = ciphertext[j*klen:(j+1)*klen]       # first chunk of guessed key length
            b = ciphertext[(j+1)*klen:(j+2)*klen] # second chunk right after
            if len(a) == klen and len(b) == klen:    # only use full chunks
                distances.append(hamming_distance(a,b) / klen)
        if distances:
            scores.append((sum(distances) / len(distances), klen))
            
    return min(scores)[1]       # key length with smallest distance is most likely correct

def break_single_byte(data: bytes) -> int:
    best_score, best_key = -1, 0
    for k in range(256):
        decrypted = bytes(b ^ k for b in data)
        score = sum(
            1 for b in decrypted
            if chr(b).lower() in "etaoin shrdlu"
        )
        if score > best_score:
            best_score, best_key = score, k
    return best_key
 
def break_repeating_xor(ciphertext: bytes, key_len: int) -> bytes:
    return bytes(
        break_single_byte(ciphertext[i::key_len])
        for i in range(key_len)
    )

a = b"Hello"
b = b"World"
print(hamming_distance(a, b))  # 14

ciphertext = xor_encrypt(b"Hello, World!", b"K")
print(break_single_byte(ciphertext))    # 75 (ASCII value of 'K')

# example — works best with long, non-repeating plaintext
message = b"In cryptography, a cipher is an algorithm for performing encryption or decryption. When we encrypt data with a repeating key, the key cycles through the plaintext. This creates a pattern that can be detected using statistical analysis."
ciphertext = xor_encrypt(message, b"SECRET")
key_len = guess_key_length(ciphertext)
print(key_len)  # 6
print(break_repeating_xor(ciphertext, key_len))  # b'SECRET'