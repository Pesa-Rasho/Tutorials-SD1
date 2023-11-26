import random
hidden = 6

random_num= random.randint(1,20)

while random_num!=hidden:
    
    print(f"{random_num} is not the number")
    random_num= random.randint(1,20)
    
print(f"{random_num} is right")