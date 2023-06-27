import random
result = []
def roll(number_of_roll):
    for i in range(1, number_of_roll + 1):
        dice = random.randrange(1, 7)
        result.append(dice)
    print("\n---------------------------")
    print(result)
    print("---------------------------")
n = int(input("Enter the numbers of rolls: "))

roll(n)