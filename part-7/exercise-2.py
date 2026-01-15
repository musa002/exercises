import string

def separate_characters(my_string: str):
    letters = ""
    punctuations = ""
    others = ""

    for ch in my_string:
        if ch in string.ascii_letters:
            letters += ch
        elif ch in string.punctuation:
            punctuations += ch
        else:
            others += ch

    return (letters, punctuations, others)


parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
print(parts[0])  
print(parts[1])  
print(parts[2])  
