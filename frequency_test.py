from collections import Counter

def frequency_test(text):
    frequencies = Counter(text)
    total_letters = sum(frequencies.values())
    for letter, count in frequencies.items():
        print(f"{letter}: {count / total_letters * 100:.2f}%")

ciphertext = "Hello, this is a test for Kryptografia's assignment."  #text to decrypt
print("Frequency test on ciphertext:")
frequency_test(ciphertext)
