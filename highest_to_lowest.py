#Batch04Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
#Input a number until the input is invalid
numbers = []
count = 1
while True:
    try:
	number = int(input(f"Enter for number {count}: "))
	numbers.append(number)
	count += 1
    except ValueError:
        #Arrange the numbers and print from highest to lowest
        arranged = sorted(numbers, reverse=True)
        print(arranged)
	break
