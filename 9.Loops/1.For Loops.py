#Do something 5 times
for i in range(5):  
    print(i)

print(list(range(5)))   #show what is the range of 5 --> [0,1,2,3,4]

#Range takes starting and ending point, excluding the ending point
#range(Start,Stop)
list(range(0,2)) #gives back [0,1]

for number in range(20,41):
    print(number)

#Add numbers in a range
    #Range(1,4) contains [1,2,3]
    #We have to add 1+2+3 and return a 6

count = 0
for number in range(1,4):
    count = count+number
print(count)


#Write a function that sums all elements of a list and return them
def sum_list(my_list):
    count=0
    for number in my_list:
        count = count+number
    return count
#assert gives us an error if statement is false, and nothing if it is true
assert sum_list([1,2,3]) == 6
assert sum_list([1,2,3,4])==10

    
