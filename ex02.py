"""
Write a function that takes a list of words (strings).
It should return a tuple containing three integers, 
representing the length of the shortest word, 
the length of the longest word, 
and the average word length.
"""

# def mysum(*args):
#     """
#     This function takes in any number of arguments and returns the sum of the numbers using a for loop.
#     """
#     total = 0
#     for i in args:
#         total += i
#     return print(f"The sum of the numbers is: {total}")

# mysum(1,2,3)
# mysum(10,20,30,40,50)


def word_lengths(words):
    word_lengths = [len(word) for word in words]
    return (min(word_lengths), max(word_lengths), sum(word_lengths)/len(word_lengths))

wordlist = ["kutya", "macska", "tehen"]

word_lengths(wordlist)