import random
computer_score=0
your_score=0
tied_game=0
total_game=0
while True:
    print("="*35,"Menu","="*35)
    print("1.Play Game\n2.Exit Game")
    game=input("Enter your Choice=")
    if game=='1' or game=='play':
        total_game=total_game+1
        choice1=['rock','paper','scissors']
        print("-"*35,"Your Choices","-"*35)
        print("Rock\nPaper\nScissors")
        user_choice=input("Enter your Choice=").lower()
        computer_choice=random.choice(choice1)
        if user_choice not in choice1:
            print("Invalid choice!")
            continue
        if ((user_choice=='paper' )and (computer_choice=='rock')) or\
            ((user_choice=='scissors') and (computer_choice=='paper')) or\
            ((user_choice=='rock' ) and (computer_choice=='scissors')):
            print("-"*85)
            print("You won!")
            your_score=your_score+1
            print(f"Your Score {your_score}")
        elif ((user_choice=='rock' )and (computer_choice=='paper')) or\
            ((user_choice=='paper' ) and (computer_choice=='scissors')) or\
            ((user_choice=='scissors') and (computer_choice=='rock')):
            print("-"*85)
            print("Computer won!")
            computer_score=computer_score+1
            print(f"Computer Score {computer_score}")
        else:
            print("-"*85)
            print("Game Tied!")
            print(f"Your Choice {user_choice} and computer choice {computer_choice} both choices are same")
            print("-"*85)
            tied_game=tied_game+1
    else:
        print("Thanks For Playing This Game")
        print("-"*85)
        print(f"Your Final score is = {your_score}")
        print("-"*85)
        print(f"Computer Final Score is = {computer_score}")
        print("-"*85)
        print(f"Total Tied Game Play = {tied_game}")
        print("-"*85)
        print(f"Total Game Played = {total_game}")
        print("-"*85)
        exit()