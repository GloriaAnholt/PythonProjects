# Code_cadamy 
# Practice Makes Perfect
# Ex 10: Censored


def censor(text, word):
    new_text = []
    for w in text.split():
        if w == word:
            new_text.append('*' * len(word))
        else:
            new_text.append(w)
    print new_text
    return " ".join(new_text)


censor("this is a pile of dicks", "dicks")
