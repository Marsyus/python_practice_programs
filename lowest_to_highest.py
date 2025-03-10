#Batch03Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
#Input a number until the input is invalid
count = 1
numbers = []
while True:
    try:
        number = int(input(f"Enter for number {count}: "))
        numbers.append(number)
        count += 1
    except ValueError:
        break
#Arrange the numbers to print from lowest to highest
