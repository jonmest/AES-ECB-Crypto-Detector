
# Constant value for AES block size
from Crypto.Cipher.AES import block_size
def aes_repetitions (ciphertext: bytes) -> int:
    all_chunks: list = []
    for i in range(0, len(ciphertext), block_size):
        all_chunks.append(ciphertext[i : i + block_size])
    return len(all_chunks) - len(set(all_chunks))
