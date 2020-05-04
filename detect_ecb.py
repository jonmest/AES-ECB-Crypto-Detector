from aes_repetitions import aes_repetitions
def detect_ecb (ciphertexts: list) -> tuple:
    # Highest probability of being ECB
    most_likely: tuple = (-1, 0)
    for i in range(len(ciphertexts)):
        reps = aes_repetitions(ciphertexts[i])
        most_likely = max(
            # Which one is greatest
            most_likely, (i, reps),
            # Going by reps
            key=lambda x:x[1])

    return most_likely