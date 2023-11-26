import random
hidden = random.randint(1,20)
guess_Count = 0

while guess_Count < 5:
    user_guess = int(input("Guess a number between 1 and 20: "))
    if user_guess == hidden:
        print("You guessed it right!")
        break
    elif user_guess < hidden:
        print("Too low")
        guess_Count += 1
    elif user_guess > hidden:
        print("Too high")
        guess_Count += 1
    else:
        print("Invalid input")
        guess_Count += 1
