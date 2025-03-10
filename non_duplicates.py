#Batch03Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#Input ten numbers
numbers = []
for i in range(1, 11):
    number = int(input(f"Enter for number {i}: "))
    numbers.append(number)
#Determine which number has a duplicate
dupes = set()
seen = set()
for each in numbers:
    if each in seen:
        dupes.add(each)
    seen.add(each)
#Print numbers without duplicates
