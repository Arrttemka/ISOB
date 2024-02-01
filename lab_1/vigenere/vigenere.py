def get_caesar_key(character):
    if 'A' <= character <= 'Z':
        return ord(character) - ord('A')
    elif 'a' <= character <= 'z':
        return ord(character) - ord('a')
    elif 'А' <= character <= 'Я':
        return ord(character) - ord('А')
    elif 'а' <= character <= 'я':
        return ord(character) - ord('а')
    elif character == 'Ё':
        return ord('Е') - ord('А') + 1
    elif character == 'ё':
        return ord('е') - ord('а') + 1
    else:
        return 0

def shift_character(character, key, alphabet_start, alphabet_length):
    return chr((ord(character) - ord(alphabet_start) + key) % alphabet_length + ord(alphabet_start))

def string_encryption_v(source_string, key):
    encrypted_string = ""

    for i in range(len(source_string)):
        caesar_key = get_caesar_key(key[i % len(key)])
        character = source_string[i]

        if 'A' <= character <= 'Z':
            encrypted_string += shift_character(character, caesar_key, 'A', 26)
        elif 'a' <= character <= 'z':
            encrypted_string += shift_character(character, caesar_key, 'a', 26)
        elif 'А' <= character <= 'Я':
            encrypted_string += shift_character(character, caesar_key, 'А', 32)
        elif 'а' <= character <= 'я':
            encrypted_string += shift_character(character, caesar_key, 'а', 32)
        elif character == 'Ё':
            encrypted_string += shift_character('Е', caesar_key, 'А', 32)
        elif character == 'ё':
            encrypted_string += shift_character('е', caesar_key, 'а', 32)
        else:
            encrypted_string += character

    return encrypted_string

def string_decoding_v(source_string, key):
    decoded_string = ""

    for i in range(len(source_string)):
        caesar_key = -get_caesar_key(key[i % len(key)])
        character = source_string[i]

        if 'A' <= character <= 'Z':
            decoded_string += shift_character(character, caesar_key, 'A', 26)
        elif 'a' <= character <= 'z':
            decoded_string += shift_character(character, caesar_key, 'a', 26)
        elif 'А' <= character <= 'Я':
            decoded_string += shift_character(character, caesar_key, 'А', 32)
        elif 'а' <= character <= 'я':
            decoded_string += shift_character(character, caesar_key, 'а', 32)
        elif character == 'Ё':
            decoded_string += shift_character('Е', caesar_key, 'А', 32)
        elif character == 'ё':
            decoded_string += shift_character('е', caesar_key, 'а', 32)
        else:
            decoded_string += character

    return decoded_string


def read_file():
    with open('input.txt', 'r', encoding='utf-8') as file:
        return file.read()

def main():

    key = 'key'  # Замените на ваш ключ

    source_string = read_file()
    encrypted_string = string_encryption_v(source_string, key)
    decoded_string = string_decoding_v(encrypted_string, key)

    print('Source String:', source_string)
    print('Encrypted String:', encrypted_string)
    print('Decoded String:', decoded_string)

if __name__ == '__main__':
    main()
