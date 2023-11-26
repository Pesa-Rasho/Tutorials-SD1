user_input=True
while user_input :
    num = input("Enter a number : ")
    try:
        num = int(num)
        print("You entered", num,".It is a number.")
        user_input=False
    except ValueError:
        print("You entered", num,".It is not a number.")
        
        
    
   
print("You have entered a correct number")