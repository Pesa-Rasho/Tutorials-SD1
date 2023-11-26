try:
    n = int(input("Give me a number over 100: "))
    if n <= 100:
        print(f"{n} is not over 100")
    else:
        print(f"{n} is over 100")
except ValueError:
    print("You didn't enter a number")
