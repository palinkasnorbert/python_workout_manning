def pl_sentence(sentence: str) -> str:
    wordlist = sentence.split(" ")
    pig_latin_words = []
    for word in wordlist:
        if word[0] in "aeiou":
            output = f"{word}way"
        else:
            output = f"{word[1:]}{word[0]}ay"
        pig_latin_words.append(output)

    return " ".join(pig_latin_words)

if __name__ == "__main__":
    print(pl_sentence('this is a test translation'))