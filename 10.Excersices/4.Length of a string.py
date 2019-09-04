#My way:
def string_length(Str):
    return len(Str)
print(string_length('Malik Omer'))

#Qazi's way:

def string_len(my_string):
    count=0
    for letter in my_string:
        #print(letter)
        count+=1
    return count

print(string_len('hello'))

