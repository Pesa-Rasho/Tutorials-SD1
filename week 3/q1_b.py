mark=input('Enter your age : ')
try:
    mark = int(mark)
    if mark>=18:
        print('You are eligible to vote')
    else:
        print('You are not eligible to vote')
except ValueError as e:
    print(f"You cannot use {mark} as input")
    print("Invalid input")