def find_max(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2
    else:
        return 'both numbers are equal'
print(find_max(3,6))
