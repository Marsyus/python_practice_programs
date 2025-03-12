#Batch04Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
#Input a number until the input is invalid
numbers = []
count = 1
while True:
    try:
	number = int(input(f"Enter for number {count}: "))
        numbers.append(number)
        count += 1
    except ValueError:
	break
#Determine which number has the most duplicates
dupes = dict()
for each in numbers:
    if each in dupes:
        dupes[each] += 1
    else:
	dupes[each] = 1
most_dupes = []
for num, dupe in dupes.items():
    if dupe == max(dupes.values()):
	most_dupes.append(num)
#Print the number
print("The most duplicated number is", most_dupes)
