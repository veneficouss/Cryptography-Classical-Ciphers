def affine_encrypt(plaintext, a, b):
    return "".join(
        chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a')) if char.islower() 
        else chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A')) if char.isupper() 
        else char for char in plaintext
    )

def affine_decrypt(ciphertext, a, b):
    m = 26
    inv_a = pow(a, -1, m)  #reverse of a mod 26
    return "".join(
        chr(((inv_a * (ord(char) - ord('a') - b)) % 26) + ord('a')) if char.islower() 
        else chr(((inv_a * (ord(char) - ord('A') - b)) % 26) + ord('A')) if char.isupper() 
        else char for char in ciphertext
    )

plaintext = "Hello, this is a test for Kryptografia's assignment."
a, b = 17, 4
encrypted_text = affine_encrypt(plaintext, a, b)
decrypted_text = affine_decrypt(encrypted_text, a, b)

print("\nAffine Cipher:")
print("Plaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
