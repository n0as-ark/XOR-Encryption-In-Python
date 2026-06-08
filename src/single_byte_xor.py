# Single-byte XOR Encryption
def xor_encrypt(plaintext: bytes, key: int) -> bytes:
    """XOR each byte with a single-byte key (from 0 to 255)."""
    return bytes(byte ^ key for byte in plaintext)

# Encryption and decryption are identical
xor_decrypt = xor_encrypt

# Example
message = b"Hello, World!"
key = 13

ciphertext = xor_encrypt(message, key)      # encrypted message
recovered = xor_decrypt(ciphertext, key)    # decrypted message

print(ciphertext)   # b'Ehaab!-Zb\x7fai,'
print(recovered)    # b'Hello, World!'