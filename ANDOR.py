text = "Hello World"
key = 127

print("Char  ASCII  AND  OR  XOR")
for ch in text:
    val = ord(ch)
    print(ch, val, val & key, val | key, val ^ key)
