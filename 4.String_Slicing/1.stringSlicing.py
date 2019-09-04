#Gets the first letter of hello, which is 'h'
'hello'[0]

#[Start:Stop]
'hello'[0:4]

#we can skip the start, if it is zero
'hello'[:3]

#if we skip the stop,it will take the last index
'hello'[0:]

#if we skip start and stop it will go from 0 to last index i-e this [:] will be [0:last index]
'hello'[:]

# [-1] will show the last index i-e 'o'
'hello'[-1]

#All of the below do the same task and delete the last 'o' from hello
'hello'[0:-1]
'hello'[0:4]
'hello'[:4]
'hello'[:-1]



