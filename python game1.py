import random
#Generate a random number between 1 and 10
secret_number = random.randint(1,10)

#Ask the user to guess
print("Guess a number between 1 and 10")

#Allow 3 attempts
for attempt in range(3):
        guess = int(input("Your guess: "))

        if guess == secret_number:
                print("Congratulations! You guessed it right.")
                break
        else:
                print("Wrong guess.Try again.")
                #Reveal the number if not guessed
                if guess != secret_number:
                        print(f"Sorry,the number was {secret_number}.Better luck next time!")
                        