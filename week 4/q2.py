total=0
count=0
num=int(input("Enter a number. If you want to quit, enter -9: "))

try:
    while num!= -9:
        total += num
        count += 1
        num=int(input("Enter a number. If you want to quit, enter -9: "))
    print("The average is", total/count)
except ZeroDivisionError as e:
    print("At least one number is required to compute the average.")

       