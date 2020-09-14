import random

def roll_dice(num_of_dice, num_of_sides):
    dice_rolls = {roll+1: 0 for roll in range(num_of_sides)}
    for i in range(num_of_dice):
        roll = random.randint(1, num_of_sides)
        dice_rolls[roll] += 1
    return dice_rolls

if __name__== "__main__":
    rolls = roll_dice(1000, 16)
    print(rolls)
    print(sum(rolls.values()))

