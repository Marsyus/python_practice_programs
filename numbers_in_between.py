#Batch02Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
#Input two numbers
num_01 = int(input("Enter first number: "))
num_02 = int(input("Enter second number: "))
#Print numbers between the two
while num_01 < num_02:
    num_01 += 1
    print(num_01)
while num_01 > num_02:
    num_01 -= 1
    print(num_01)
