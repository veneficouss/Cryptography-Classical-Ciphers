def vigenere_encrypt(plaintext, key):
    key_repeated = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    return "".join(
        chr((ord(char) - ord('a') + ord(k) - ord('a')) % 26 + ord('a')) if char.islower()
        else chr((ord(char) - ord('A') + ord(k.upper()) - ord('A')) % 26 + ord('A')) if char.isupper() 
        else char for char, k in zip(plaintext, key_repeated)
    )

def vigenere_decrypt(ciphertext, key):
    key_repeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    return "".join(
        chr((ord(char) - ord('a') - (ord(k) - ord('a')) + 26) % 26 + ord('a')) if char.islower()
        else chr((ord(char) - ord('A') - (ord(k.upper()) - ord('A')) + 26) % 26 + ord('A')) if char.isupper() 
        else char for char, k in zip(ciphertext, key_repeated)
    )

plaintext = "Hello, this is a test for Kryptografia's assignment."
key = "BCD"
encrypted_text = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(encrypted_text, key)

print("\nVigenere Cipher:")
print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
