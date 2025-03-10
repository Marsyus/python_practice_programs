#Batch01Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
#Iterate from 0 to 100
for i in range(101):
    #Print the numbers not ending in zero
    if i % 10:
        print(i)
