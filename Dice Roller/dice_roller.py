import random

def roll_dice(num_dice):
    result = []
    for i in range(num_dice):
        roll = random.randint(1, 6)
        result.append(roll)
    return result

num_dice = int(input("Enter the number of dice : "))
dice_results = roll_dice(num_dice)
print("You rolled: ", dice_results)
print("Total: ", sum(dice_results))
