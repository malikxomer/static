#if
#else
#else if or elif in python
#Rock paper Scissors--> Rock wins in this game

human = 'rock'
computer = 'scissors'
if human == 'rock' and computer == 'scissors':
    human_score = 1


# Now checking with else if
computer = 'banana'
if human == 'rock' and computer == 'scissors':
    human_score = 1
elif human == 'rock' and computer == 'banana':
    computer_score=0
    human_score=0
    print('you cant pick anything other than rock and scissors')

# Checking if anyone picked wrong
if human == 'banana' or computer == 'banana':
    print('wrong input')

#Checking by other way
if computer != 'rock' or computer !='scissors' or computer !='paper':
    print("WRONG CHOICE,PICK AGAIN")



