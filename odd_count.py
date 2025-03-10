#Batch01Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#Input ten numbers
count = 0
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    #Count the odd numbers
    if number % 2:
        count += 1
#Print the count
print(f"There are {count} odd numbers")
