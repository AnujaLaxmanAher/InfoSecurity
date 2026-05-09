def encrypt(text, key):
    col = len(key)
    matrix = [''] * col

    # Fill columns
    for i in range(len(text)):
        column = i % col
        matrix[column] += text[i]

    # Arrange columns based on sorted key
    cipher = ''
    for k in sorted(range(len(key)), key=lambda x: key[x]):
        cipher += matrix[k]

    return cipher


def decrypt(cipher, key):
    col = len(key)
    length = len(cipher)
    rows = length // col

    matrix = [''] * col
    order = sorted(range(len(key)), key=lambda x: key[x])

    start = 0
    for i in order:
        matrix[i] = cipher[start:start+rows]
        start += rows

    text = ''
    for i in range(rows):
        for j in range(col):
            text += matrix[j][i]

    return text


# Main
print("----- Transposition Cipher -----")

text = input("Enter the plaintext: ")
key = input("Enter the key: ")

cipher = encrypt(text, key)
print("Ciphertext:", cipher)

plain = decrypt(cipher, key)
print("Decrypted text:", plain)