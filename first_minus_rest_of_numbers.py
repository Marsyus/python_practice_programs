#Batch02Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#Input ten numbers
first_num = 0
numbers = []
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    numbers.append(number)
    #Compute the first number minus the rest
    if i == 1:
        first_num = number
    else:
        first_num -= number
#Print the result
