#Batch04Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
#Input a number until the input is invalid
numbers = []
count = 1
while True:
    try:
	number = int(input(f"Enter for number {count}: "))
	numbers.append(number)
	count += 1
    except ValueError:
        #Arrange the numbers to find and print the highest
        arranged = sorted(numbers, reverse=True)
        print(arranged[0])
	break
