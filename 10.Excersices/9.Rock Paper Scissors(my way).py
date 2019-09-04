#Rules for the game
# rock vs rock == draw
# rock vs paper == paper wins
# rock vs scissor == rock wins

# paper vs paper == draw
# paper vs rock == paper wins
# paper vs scissors == scissors wins

# scissors vs scissors == draw
# scissors vs paper == scissors wins
# scissors vs rock == rock wins

import random

#Global variable thal all function know about.
#DO NOT EDIT THESE GLOBAL VARIABLES
#OR YOUR GAME WILL BREAK

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

def choice_to_number(choice):
    """Convert Choice to number."""
    #If choice is rock, give back 0
    #If choice is paper, give back 1
    #If choice is scissors, give back 2
    return {'rock':0 , 'paper':1 , 'scissors':2}[choice]

def number_to_choice(number):
    """Convert Number to choice."""
    #If choice is 0, give back rock
    #If choice is 1, give back paper
    #If choice is 2, give back scissors
    return {0:'rock' , 1:'paper' , 2:'scissors'}[number]

def random_computer_choice():
    """Choose randomly for computer"""
    #lookup random.choice()
    choice = random.randint(0,2)
    return number_to_choice(choice)
# or we can use return random.choice(['rock' , 'paper' , 'scissors'])

def choice_result(human_choice,computer_choice):
    """Return the result of who wins"""
    #DO NOT REMOVE THESE GLOBAL VARIABLE LINES.
    #we specified them to say that we want the variables in the main program to change their values
    global COMPUTER_SCORE
    global HUMAN_SCORE
    
    # based on the given human_choice and computer_choice
    # determine who won and increment their score by 1.
    # if tie, then don't increment anyone's score

    #example code
    # if human_choice == 'rock' and computer_choice == 'paper':
    #       COMPUTER_SCORE = COMPUTER_SCORE +1
    
    if human_choice == 'rock' and computer_choice == 'paper':
        COMPUTER_SCORE = COMPUTER_SCORE +1
        return COMPUTER_SCORE
    elif human_choice == 'rock' and computer_choice == 'scissors':
        HUMAN_SCORE = HUMAN_SCORE+1
        return HUMAN_SCORE
    elif human_choice == 'rock' and computer_choice == 'rock':
        return 'same'
        
    elif human_choice == 'paper' and computer_choice == 'rock':
        HUMAN_SCORE = HUMAN_SCORE+1
        return HUMAN_SCORE
    elif human_choice == 'paper' and computer_choice == 'scissors':
        COMPUTER_SCORE = COMPUTER_SCORE +1
        return COMPUTER_SCORE
    elif human_choice == 'paper' and computer_choice == 'paper':
        return 'same'
        
    elif human_choice == 'scissors' and computer_choice == 'paper':
        HUMAN_SCORE = HUMAN_SCORE+1
        return HUMAN_SCORE
    elif human_choice == 'scissors' and computer_choice == 'rock':
        COMPUTER_SCORE = COMPUTER_SCORE +1
        return COMPUTER_SCORE
    elif human_choice == 'scissors' and computer_choice == 'scissors':
        return 'same'
    else:
        print('Hello')
      

###############################
#DO NOT REMOVE THESE TEST FUNCTIONS.
#THEY WILL TEST YOUR CODE
def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'

def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2

def test_all():
    test_choice_to_number()
    test_number_to_choice()

#Uncomment the line below to test your code
test_all()

###############################
human_choice = number_to_choice(1)
computer_choice = random_computer_choice()
choice_result(human_choice,computer_choice)

print("computer score == ",COMPUTER_SCORE)
print("human score == ",HUMAN_SCORE)
print('human choice == ',human_choice)
print("random computer choice == ",computer_choice)
