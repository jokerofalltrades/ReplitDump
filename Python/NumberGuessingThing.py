import random

secretNum = random.randint(1,100)
uInput = int(input("Guess a number between 1 and 100: "))

while uInput != secretNum:
    if uInput > secretNum:
        uInput = int(input("Your guess was larger than the secret number, guess another number: "))
    else:
        uInput = int(input("Your guess was smaller than the secret number, guess another number: "))
print("Wow! you guessed it.")
