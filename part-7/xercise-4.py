import random

def words(n: int, beginning: str):
    with open("words.txt") as f:
        all_words = [line.strip() for line in f if line.strip()]

    matching_words = [w for w in all_words if w.startswith(beginning)]
    if len(matching_words) < n:
        raise ValueError(f"Not enough words starting with '{beginning}'")
    
    return random.sample(matching_words, n)


word_list = words(3, "ca")
for word in word_list:
    print(word)
