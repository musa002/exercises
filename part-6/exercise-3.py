import enchant

def spell_check():
    dictionary = enchant.Dict("en_US")
    text = input("Write text: ")
    words = text.split()
    checked_words = []

    for word in words:
        clean_word = word.strip(".,!?;:")
        if dictionary.check(clean_word):
            checked_words.append(word)
        else:
            checked_words.append(f"*{word}*")

    print(" ".join(checked_words))

spell_check()
