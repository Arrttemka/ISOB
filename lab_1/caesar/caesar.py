def caesar_encrypt(text, shift):
    english_alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    english_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    russian_alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    russian_alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    encrypted_text = ''

    for char in text:
        if char in english_alphabet_lower:
            index = (english_alphabet_lower.index(char) + shift) % len(english_alphabet_lower)
            encrypted_text += english_alphabet_lower[index]
        elif char in english_alphabet_upper:
            index = (english_alphabet_upper.index(char) + shift) % len(english_alphabet_upper)
            encrypted_text += english_alphabet_upper[index]
        elif char in russian_alphabet_lower:
            index = (russian_alphabet_lower.index(char) + shift) % len(russian_alphabet_lower)
            encrypted_text += russian_alphabet_lower[index]
        elif char in russian_alphabet_upper:
            index = (russian_alphabet_upper.index(char) + shift) % len(russian_alphabet_upper)
            encrypted_text += russian_alphabet_upper[index]
        else:
            encrypted_text += char

    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)


with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

shift = 3

encrypted_text = caesar_encrypt(text, shift)
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_decrypt(encrypted_text, shift)
print(f"Decrypted: {decrypted_text}")
