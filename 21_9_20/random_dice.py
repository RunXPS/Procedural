from sys import argv
import random
def roll_dice():
    return (random.randint(1,6), random.randint(1,6))
number_of_trials = int(input("Enter a number: "))
tally = {}
for k in range(number_of_trials):
    roll = roll_dice()
    if sum(roll) in tally:
        tally[sum(roll)] += 1
    else:
        tally[sum(roll)] = 1

order = sorted(tally.keys())
for result in order:
    #dictionary iterator presents keys
    print(f"{result}\t\t {tally[result]}")