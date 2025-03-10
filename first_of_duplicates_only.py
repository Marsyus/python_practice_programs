#Batch03Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#Input ten numbers
numbers = []
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    numbers.append(number)
#Print all numbers without duplicating
print(set(numbers))
