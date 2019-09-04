# We use while loops when we don't know when it is going to stop
# We use for loops when we know when it is going to stop
#   While ( CONDITION )  -->  True
#       THEN THIS
# Condtion example:
#       5<6 --> True, so the loop will run
#       5>6 --> False, so the loop won't run

count = 0
while count < 100:
    print(count)
    count=count+1
#    if count == 70:
#       break

# ============= Practice =============
# Print from 100 to 1 and instead of zero print 'blast off'
count = 100
while count>0:
    print(count)
    count=count-1
    if count==0:
        print('blast off')
