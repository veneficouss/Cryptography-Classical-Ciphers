def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted = (ord(char.lower()) - ord('a') + shift) % 26 + ord('a')
            ciphertext += chr(shifted) if char.islower() else chr(shifted).upper()
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

plaintext = "Hello, this is a test for Kryptografia's assignment."
shift = 3
encrypted_text = caesar_encrypt(plaintext, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("\nCaesar Cipher:")
print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
