import random 
# Possible moves 
moves = ['rock','paper','scissors']

#get user's choice 
user_move = input("Choose rock,paper or scissors: ").lower()

#Get computer's random choice 
computer_move = random.choice(moves)

print(f"Computer chose:{computer_move}")

#determine winner 
if user_move == computer_move:
    print("It's a tie!")
elif(
    (user_move == 'rock' and computer_move == 'scissors') or \
    (user_move == 'scissors' and computer_move == 'paper') or \
    (user_move == 'paper' and computer_move == 'rock')):
        print("You win!")
else:
        print("You lose!")