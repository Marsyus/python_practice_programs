#Batch02Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#Input ten numbers
numbers = []
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    numbers.append(number)
#Count the even numbers
count = 0
for even in numbers:
    if even % 2 == 0:
        count += 1
#Print the count
print(f"There are {count} even numbers")
