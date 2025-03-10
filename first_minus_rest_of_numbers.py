#Batch02Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#Input ten numbers
numbers = []
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    numbers.append(number)
#Compute the first number minus the rest
#Print the result
