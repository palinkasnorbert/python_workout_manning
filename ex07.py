def ubbi_dubbi(word: str) -> str:
    """
    every vowel (a, e, i, o, or u) is prefaced with ub
    """
    
    new_word = []
    for l in word:
        if l.lower() in "aeiou":
            new_word.append(f"ub{l}")
        else:
            new_word.append(l)
    return "".join(new_word).capitalize()

print(ubbi_dubbi("Milk"))
print(ubbi_dubbi("octopus"))
print(ubbi_dubbi("Elephant"))
print(ubbi_dubbi("soap"))