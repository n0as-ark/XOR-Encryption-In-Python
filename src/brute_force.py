# brute_force.py
# Attempts to decrypt XOR-encrypted ciphertext by trying all 256 possible single-byte keys.
# Prints results that decode as valid UTF-8 and contain spaces,
# since natural language text almost always has spaces while random bytes rarely do.


# Single-byte XOR Encryption
def xor_encrypt(plaintext: bytes, key: int) -> bytes:
    """XOR each byte with a single-byte key (from 0 to 255)."""
    return bytes(byte ^ key for byte in plaintext)

# Encryption and decryption are identical
xor_decrypt = xor_encrypt

def brute_force(ciphertext: bytes) -> None:
    for key in range(256):  # try every possible single-byte key
        attempt = xor_decrypt(ciphertext, key)
        try:
            text = attempt.decode("utf-8")  # fails if result is not valid text
            if " " in text:                 # spaces suggest readable output
                print(f"Key {key}: {text}")
        except UnicodeDecodeError:
            pass                            # skip keys that produce invalid text
