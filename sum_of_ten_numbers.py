#Batch01Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#Input ten numbers
numbers = []
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    numbers.append(number)
#Print the sum of the numbers
print("The sum is", sum(numbers))
