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
