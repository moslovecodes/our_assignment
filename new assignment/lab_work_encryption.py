
letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key 
                if new_index >= 26:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key 
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
    return plaintext

print()
print('*** ENCRYPTION AND DECRYPTION PROGRAM***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('Please enter letter "e" for encryption or letter "d" for decryption: ').lower()
print()

if user_input == 'e': 
    print('LET ME ENCRYPT FOR YOU')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('LET ME DECRYPT FOR YOU')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')