#Batch01Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#Input ten numbers
numbers = []
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    numbers.append(number)
#Count the odd numbers
count = 0
for odd in numbers:
    if odd % 2:
        count += 1
#Print the count
print(f"There are {count} odd numbers")
