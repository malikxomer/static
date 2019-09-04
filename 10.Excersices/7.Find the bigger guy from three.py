# My solution
def find_max(num1,num2,num3):
    if num1>num2:
        if num1>3:
            return num1
        elif num1<num3:
            return num3
        else:
            return 'num1 and num3 are equal'
    elif num2>num1:
        if num2>num3:
            return num2
        elif num2<num3:
            return num3
        else:
            return 'num2 and num3 are equal'
    else:
        return 'All numbers are equal'
print(find_max(8,8,8))

#######################
# Qazi's solution
def find_bigger(guy1,guy2,guy3):
    if guy1>guy2:
        bigger_guy = guy1
    else:
        bigger_guy = guy2

    if bigger_guy > guy3:
        biggest_guy=bigger_guy
    else:
        biggest_guy=guy3
    return biggest_guy
    
print(find_bigger(16,234,111))

##########################
# One line solution
def bigger_guy(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def biggest_guy(num1,num2,num3):
    return bigger_guy(bigger_guy(num1,num2),num3)

print(biggest_guy(50,40,30))

#########################
#Python built in function
def big_num(number1,number2,number3,number4):
    return max(number1,number2,number3,number4)
print(max(30,10,40,20))
