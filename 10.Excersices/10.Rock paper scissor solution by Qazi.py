import random

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

def choice_to_number(choice):
    """Convert Choice to number."""
    my_dict = {'rock':0 , 'paper':1 , 'scissors':2}
    return my_dict[choice]

def number_to_choice(number):
    my_dict = {0:'rock' , 1:'paper' , 2:'scissors'}
    return my_dict[number]

def random_computer_choice():
    """Choose randomly for computer"""
    random.choice(['rock' , 'paper' , 'scissors'])

def choice_result(human_choice,computer_choice):
    """Return the result of who wins"""
    global COMPUTER_SCORE
    global HUMAN_SCORE

    human_number = choice_to_number(human_choice)
    computer_choice = choice_to_number(computer_choice)

# Anything % 3 == a number between 0-2
# [0,1,2]  == [rock, paper, scissors]
# rocks vs scissors
# (0-2) % 3 == 1
# (-2) % 3 == 1
# 1 == 1
# rock wins
#
#paper vs scissors
# (paper - scissors) % 3 == 1
# (1-2) % 3 == 1
# 2 == 1
# scissors wins
#
# paper vs rocks
# (paper - rocks) % 3 == 1
# (1-0) % 3 == 1
# 1 %3 == 1
# 1 == 1
# paper wins
    if (human_number - computer_number) % 3 == 1:
        COMPUTER_SCORE +=1
    elif human_number == computer_number:
        print('Tie')
    else:
        HUMAN_SCORE +=1


###############################
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

