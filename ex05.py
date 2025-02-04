def pig_latin(word):
    
    if word[0].lower() in "aeiou":
        output = f"{word}wayuppercasefirstletter"
    
    output = f"{word[1:]}{word[0]}ay"

    if word[0].isupper():
        output = output.capitalize()

    return output
    
print(pig_latin("Air"))
print(pig_latin("air"))
print(pig_latin("Python"))
print(pig_latin("python"))