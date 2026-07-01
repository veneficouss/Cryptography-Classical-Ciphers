# Cryptography — Classical Cipher Implementations

**Course:** Cryptography — Assignment 1
**Semester:** 3rd
**Student:** Marinos Matthaiou — inf2023004
**Date:** November 2024

## Overview

This assignment covers three classical substitution ciphers — **Caesar**, **Affine**, and **Vigenère** — analyzed both through **CrypTool** (visual/theoretical analysis, brute-force attacks, frequency analysis) and implemented from scratch in **Python**.

The full written report (`Report_Assignment.pdf`) covers:
- **Section A** — theoretical description of how each cipher works, tested in CrypTool
- **Section B** — frequency analysis of the ciphertexts and comparison between ciphers
- **Section C** — brute-force attacks on Caesar and Vigenère (Affine excluded per instructor's note, no CrypTool component available)
- **Section D** — the Python implementations in this repo, each paired with a frequency test

## Repository Structure

```
.
├── caesar_cipher.py       # Caesar cipher: encrypt/decrypt via fixed alphabet shift
├── affine_cipher.py       # Affine cipher: encrypt/decrypt via E(x) = (a*x + b) mod 26
├── vigenere_cipher.py      # Vigenère cipher: encrypt/decrypt via repeating keyword shift
├── frequency_test.py       # Letter frequency analysis on a given text
└── Report_Assignment.pdf # Full written report (CrypTool analysis, brute-force attacks, findings)
```

## How to Run

Each script is self-contained and runs independently:

```bash
python caesar_cipher.py
python affine_cipher.py
python vigenere_cipher.py
python frequency_test.py
```

No external dependencies — pure Python standard library.

## Key Findings

- **Caesar** and **Affine** ciphers preserve the statistical letter-frequency shape of the plaintext (just shifted), making them vulnerable to frequency analysis.
- **Vigenère** produces a flatter, more uniform letter distribution, since each letter is shifted differently based on the keyword — making it harder to break via simple frequency analysis.
- Longer Vigenère keywords further flatten the distribution, increasing resistance to cryptanalysis, while short keywords still leak some pattern.

## Tools / Language

- Python 3 (standard library only)
- CrypTool (for the theoretical analysis and brute-force components — see the report)
