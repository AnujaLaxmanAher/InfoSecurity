plaintext = "DATAPROTECTION22"
ascii_values = []
for i in range(16):
    ascii_values.append(ord(plaintext[i]))

print("4x4 ASCII Matrix:\n")
index = 0
for row in range(4):
    for col in range(4):
        print(ascii_values[index], end=" ")
        index += 1
    print()






plaintext = "DATAPROTECTION22"
key = "SECUREKEY1234567"
p_ascii = []
k_ascii = []
for i in range(16):
    p_ascii.append(ord(plaintext[i]))
    k_ascii.append(ord(key[i]))
   
cipher = []
for i in range(16):
    cipher.append(p_ascii[i] ^ k_ascii[i])

print(" Result after XOR in 4x4 matrix:\n")
index = 0
for row in range(4):
    for col in range(4):
        print(cipher[index], end=" ")
        index += 1
    print()