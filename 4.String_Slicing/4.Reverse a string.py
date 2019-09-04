# By using string slicing
data = "atoyot"
stringlength = len(data)   # calculates length of string
slicedstring = data[stringlength::-1]    # Reverse the String
print (slicedstring)     # Print the string



# By Using a loop, Returns the string in the form of a list
data = "ikuzus"
reversedString = []
index = len(data)     # Calculate length of string and save in index
while index> 0:
    reversedString += data[index-1]    #save the value of data[index-1] in reverseString
    index = index - 1
print(reversedString)



# By using join condition
data = 'adnoH' #initial string
reversed=''.join(reversed(data))    # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversed)      #print the reversed string

