plaintext = "DATAPROTECTION22"
key = "SECUREKEY1234567"
def to_ascii(text):
    values = []
    for i in range(16):
        values.append(ord(text[i]))
    return values
def rotate_key(k, r):
    shift = r % 16
    return k[shift:] + k[:shift]
def print_matrix(data):
    index = 0
    for row in range(4):
        for col in range(4):
            print(data[index], end=" ")
            index += 1
        print()
state = to_ascii(plaintext)
round_key = to_ascii(key)
print("Round 0 (Initial XOR):")
for i in range(16):
    state[i] = state[i] ^ round_key[i]
print_matrix(state)
print()
for r in range(1, 11):
    round_key = rotate_key(round_key, r)
    for i in range(16):
        state[i] = state[i] ^ round_key[i]
    print("Round", r, ":")
    print_matrix(state)
    print()