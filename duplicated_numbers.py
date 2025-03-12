#Batch04Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#Input ten numbers
numbers = []
for i in range(1, 11):
    num = int(input(f"Enter for number {i}: "))
    numbers.append(num)
#Determine which number has a duplicate
dupes = set()
seen = set()
for each in numbers:
    if each in seen:
	dupes.add(each)
    seen.add(each)
#Print all numbers with duplicates
print(list(dupes))
