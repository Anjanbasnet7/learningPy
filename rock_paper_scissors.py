"""Rock beats Scissors (rock smashes scissors)

Scissors beats Paper (scissors cuts paper)

Paper beats Rock (paper somehow covers rock)"""

import random
win = 0
lose = 0
no =0
while True:
    user = input("Enter your choice(rock , paper , scissors):").strip().lower()
    computer = random.choice(["rock" , "paper" , "scissors"])
    
    if user not in ["rock", "paper" , "scissors"]:
        print("Invalid input. Choose from(rock,paper,scissors)")
    elif user == computer:
        print("It's tie!")
        no-=1
    elif user == "rock" and computer == "scissors":
        print("Rock smashes scissors. You win!")
        win+=1

    elif user == "scissors" and computer == "paper":
        print("Scissors cuts paper. You win!")
        win+=1
    elif user == "paper" and computer == "rock":
        print("Paper covers rock. You win!")
        win+=1
    else:
        print(f"You chose {user} and computer choice {computer}. You lose!")
        lose+=1

    no+=1
    if no == 5:
        print(f"Your wins time is  {win} and losses is {lose}")
        quit_game = input("Do you want to quit the game(y,n):")
        if quit_game == "y":
            break
        else:
            win = 0
            lose = 0
            no = 0

            
