#Batch02Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
#Iterate from 0 to 100
for i in range(101):
    #Print the numbers not ending in zero or five
    if i % 5:
        print(i)
