import random
secret_number = random.randint(1,100)
guess = -1
while guess != secret_number:
    guess = int(input("Enter a guess: "))
    if guess < secret_number:
        print(f"Your guess, {guess} is too low")
    elif guess > secret_number:
        print(f"Your guess, {guess} is too high")

print("Your guessed it")

#I hate break and continue
#They void the garantee the preticate is false when the loop ends.