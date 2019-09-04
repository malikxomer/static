# give choice to get back a name
def number_to_choice(choice):
    if choice==1:
        return 'Usain'
    elif choice==2:
        return 'Me'
    elif choice==3:
        return 'Qazi'
    else:
        return 'Not a member of race'

# give name to get back a position

def choice_to_number(choice):
    if choice=='Usain':
        return 1
    elif choice=='Me':
        return 2
    elif choice=='Qazi':
        return 3
    else:
        return 'Not a member of race'

print(number_to_choice(2))
print(choice_to_number('Qazi'))

##########################
#Using dictionary to solve the same problem

def num_to_choice(number):
    return {1:'Usain',2:'Me',3:'Qazi'}[number]

def choice_to_num(name):
    return {'Usain':1,'Me':2,'Qazi':3}[name]
print(num_to_choice(3))
print(choice_to_num('Usain'))    
