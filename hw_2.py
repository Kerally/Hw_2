import math


print("Task #1")
name = input("Enter your name: ")
print("Hello,", name, end="!\n")


print("Task #2")
number_1 = int(input("Please enter an integer number: "))
print("Previous number for number", number_1, "is", number_1 + 1, end=".\n")
print("Next number for number", number_1, "is", number_1 - 1, end=".\n")


print("Task #3")
v = int(input("Enter speed: "))
if v <= 0:
    print("Distance: 0")
else:
    difference = 100 // v
    print("The time haven`t be more than: ", difference)
    t = int(input("Enter time: "))
    if difference >= t >= 0:
        s = v * t
        print("Distance:", s)
    else:
        print("Incorrect input")


print("Task #4")
year = int(input("Enter the year: "))
if year % 4 == 0 or year % 400 == 0:
    if year % 100 == 0:
        print("No")
    else:
        print("YES")


print("Task #5")
input_x = float(input("Enter the x: "))
if 1 >= input_x > 0:
    print("sign(x) = 1")
elif input_x == 0:
    print("sign(x) = 0")
elif -1 <= input_x < 0:
    print("sign(x) = -1")
else:
    print("Enter the 'x' again")


print("Task #6")
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
number = int(input("Ener the number: "))
if abs(number) in list:
    print("hoo")


print("Task #7")
input_number = int(input("Enter the number: "))
for i in range(1, input_number + 1):
    print("*")

input_number = int(input("Enter the number: "))
print("*" * input_number)
