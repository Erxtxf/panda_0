true_age = int(26)

index = 0

while index <= 3:
    age = int(input('Guess a number: '))
    if age == true_age:
        print(f"You are correct")
        break
        pass
    if age > true_age:
        print(f"You are wrong, {age} is higher.")
        pass
    elif age < true_age:
        print(f"You are wrong, {age} is lower.")
        pass
    index += 1
    if index == 3 :
        print("No more chances.")
        break
        pass








