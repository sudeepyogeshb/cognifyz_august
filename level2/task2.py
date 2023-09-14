import random
n=random.randrange(1,100)
guess=int(input("Guess a number:"))

while n!=guess:
    if guess<n:
        print("Too Low, try again!")
        guess=int(input("Guess a number:"))
    elif guess>n:
        print("Too High, try again!")
        guess=int(input("Guess a number:"))
    else:
        break
print("Congratulations! your guess is right")