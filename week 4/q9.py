user_Preference = True
while user_Preference==True:
    
    try:
        user_INPUT = int(input("Enter a number "))
        if user_INPUT ==1:
            print("1 selected")
            continue
        elif user_INPUT ==2:
            print("2 selected")
            continue
        elif user_INPUT ==3:
            print("3 selected")
            continue
        elif user_INPUT ==4:
            print("4 selected")	
            print("Thank you for using the program")
            break
        else:
            print("Invalid input")
    except ValueError as e:
        print("Required input is a number")

