def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char  
    return result

# Example 
text = "Hello, World!"
shift = 3

encrypted_text = caesar_cipher(text, shift, mode='encrypt')
decrypted_text = caesar_cipher(encrypted_text, shift, mode='decrypt')

print("Original:", text)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
