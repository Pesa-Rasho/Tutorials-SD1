userInput = input("Do you like python?")
userInput = userInput.lower()
if userInput == "yes" or userInput == "y":
    print("You like python")
elif userInput == "no" or userInput == "n":
    print("You don't like python")
else:
    print("You didn't enter yes or no")