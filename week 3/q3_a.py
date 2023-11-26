import random

def printConvertedTemperature(conversion: str,celcius: float,fahrenheit: float):
    if(conversion=='celcius'):
        print(f"The temperature in celcius is {celcius}")
    else:
        print(f"The temperature in fahrenheit is {fahrenheit}")




choice=input("""
             Welcome to temperature converter
            Pick an option:
                   1-Celcius to Fahrenheit
                   2-Fahrenheit to Celcius
""")

try:
    choice =int(choice)
except ValueError as e:
    print("Please enter a valid option")
    exit(1)

if choice==1:
    celcius=input("Enter the temperature in celcius: ")
    try:
        celsius = float(celcius)
    except ValueError as e:
        print("Please enter a valid temperature")
        exit(1)
    fahrenheit = (celsius * 9/5) + 32
    printConvertedTemperature(conversion="fahrenheit",celcius=celcius,fahrenheit=fahrenheit)   
elif choice==2:
    fahrenheit=input("Enter the temperature in fahrenheit: ")
    try:
        fahrenheit = float(fahrenheit)
    except ValueError as e:
        print("Please enter a valid temperature")
        exit(1)
    celcius = (fahrenheit - 32) * 5/9
    printConvertedTemperature(conversion="celcius",celcius=celcius,fahrenheit=fahrenheit)

else:
    print("Please enter a valid option")