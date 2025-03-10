#Batch02Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
#Input two numbers
num_01 = int(input("Enter first number: "))
num_02 = int(input("Enter second number: "))
#Print the smaller number
if num_01 < num_02:
    print(f"{num_01} is smaller")
elif num_01 > num_02:
    print(f"{num_02} is smaller")
