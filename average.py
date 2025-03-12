#Batch04Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#Input a number until the input is invalid
numbers = []
count = 1
while True:
    try:
	number = int(input(f"Enter for number {count}: "))
	numbers.append(number)
	count += 1
    except ValueError:
        #Compute for the average of all numbers
        average = sum(numbers) / len(numbers)
	break
#Print the result
