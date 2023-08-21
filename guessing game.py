# Guessing Game
import random

def guess_the_number():
    random_no = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("\n Go all out! Guess the number between 1 and 100: "))
        attempts += 1

        if guess < random_no:
            print("Sorry,it's too low! Retry again.")
        elif guess > random_no:
            print("Oh no,it's too high! Give it another go.")
        else:
            print(f"Good job dude, You hit the spot! The number was {random_no}. You got it in {attempts} tries.")
            break

if __name__ == '__main__':
    guess_the_number()



                                                            #AN