# XOR Encryption in Python

A simple Python project that implements XOR encryption from scratch for learning purposes.

This repository is built to understand how encryption works at the byte level by starting with one of the simplest possible ciphers: XOR. The goal is not to create a secure encryption tool for real world use, but to study how a basic reversible operation can transform plaintext into ciphertext, and why weak designs fail so easily.

## Why this project exists

Many people first encounter "encryption" as a password prompt on a file or app. But real encryption is not just about hiding access behind a password. It depends on how data is transformed, how keys are handled, and how resistant the system is to brute force or known plaintext attacks.

XOR is a useful starting point because it is easy to implement and easy to understand. At the same time, it also shows very clearly why simplicity alone does not mean security. A single byte XOR key has only 256 possible values, which makes brute force attacks practical.

## What is XOR

XOR stands for exclusive OR. It is a bitwise operation that compares two bits and returns `1` if they are different and `0` if they are the same.

| A | B | A XOR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

One reason XOR is interesting in cryptography is that applying the same key twice restores the original value.

```python
5 ^ 3  # 6
6 ^ 3  # 5
```

Because of this property, encryption and decryption can use the same operation.

## Project goals

This repository is meant to document the process of building XOR encryption from scratch and learning from its limitations.

Planned goals include:

- Implement single byte XOR encryption and decryption
- Read and write data as raw bytes
- Show how brute force attacks work against small key spaces
- Explore known plaintext weaknesses
- Compare XOR with stronger modern encryption designs at a conceptual level

## What this project will cover

This project focuses on the mechanics of XOR encryption in Python, including:

- Converting text into bytes
- Applying XOR to each byte
- Recovering plaintext with the same key

## Important note

This project is for educational purposes only.

XOR by itself is not secure enough to protect real world sensitive data. In practice, modern encryption relies on well studied algorithms, large key sizes, secure modes of operation, and proper key derivation. This repository is intended to help build intuition, not to replace real cryptographic tools.

## Disclaimer

This repository is created to study basic cryptographic ideas in a controlled and educational context.

It should not be used as a production security tool, and it should not be relied on to protect personal, financial, medical, or other sensitive information.

## License

This project is licensed under the MIT License.

See the [LICENSE](./LICENSE) file for details.
