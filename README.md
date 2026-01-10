# Caesar Cipher - Python Implementation

This project implements a Caesar Cipher for encryption and decryption. 
Developed as part of my ADS (Analysis and Systems Development) portfolio.

# Logic & Architecture
Instead of using complex loops, this implementation utilizes the `str.maketrans` and `translate` methods for O(n) efficiency. 

# Key Feature: Bidirectional Shift
To handle decryption accurately within Python's string slicing, the formula `26 - shift` is applied when `encrypt=False`. This ensures the alphabet rotation is always mathematically sound.

#How to use

Clone the repository.

Run the script:
python Caesar_Cipher.py

Choose between encryption or decryption and set your shift value.
