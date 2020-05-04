from detect_ecb import detect_ecb

items = [bytes.fromhex(line.strip()) for line in open("text.txt")]
result = detect_ecb(items)

print("The ciphertext that most likely is AES-ECB is:",
result[0],
"\nWe found", result[1], "repetitions in it.")

# Check that the detection works correctly
assert result[0] == 132
