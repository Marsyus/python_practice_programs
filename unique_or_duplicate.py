#Batch03Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
#Input a number until the input is invalid
numbers = []
count = 1
while True:
    try:
        number = int(input(f"Enter for number {count}: "))
        count += 1
        numbers.append(number)
    except ValueError:
        break
#Print "Unique" if the number is not a duplicate. Otherwise, print "Duplicate"
