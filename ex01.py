import random

def guessing_game():
    number = random.randint(0, 100)
    
    print(number)
    round = 3
    while round > 0 and True:
        guess = input(f"Rounds left: {round}, Please guess a number between 0 and 100!\n")
        if int(guess) > number:
            print("Your guess is too high!")
            round -= 1
        if int(guess) < number:
            print("Your guess is too low!")
            round -= 1
        if int(guess) == number:
            print("Your guess is right!")
            break

if __name__ == "__main__":
    guessing_game()