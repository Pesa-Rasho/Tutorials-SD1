import random
count = 0
user_Preference = True
dice1=0
dice2=0
for i in range(100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(f"{dice1}:{dice2}")
    if dice1==dice2:
        count +=1
    else:
        continue

print(f"Out of 100 you rolled {count} doubles")