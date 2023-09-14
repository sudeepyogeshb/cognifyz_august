import random
number=random.randint(1,100)
solved=False

print("Guess a number")
while not solved:
    guess=int(input())

    if guess>number:
        print("Hint: too high, try again!")
    elif guess<number:
        print("Hint: too low, try again!")
    else:
        print("Nice! your guess is right")
        solved=True