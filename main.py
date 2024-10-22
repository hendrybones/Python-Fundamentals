# This is my python file
print("Hendry will be great this time")

# Variable = A container for a value (string,integer,float boolean)
#            A variable behaves as if it was the value it contains.

# Each variable should have a unique name.
# Strings
first_name = "Hendry"
food = "Meat"
email ="hendrymwamburi56@gmail.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# Integers
age = 25
quantity = 3
num_of_students = 30

print(f"Your age is {age}")
print(f"You are buying {quantity} items")
print(f"You have {num_of_students} students")

# Floats
price = 10.99
gpa =3.3
distance =3.5

print(f"The price is {price}")
print(f"The GPA is {gpa}")
print(f"The distance is {distance}")

# Boolean

is_student = False

if is_student:
    print("You are a student")
else:
    print("You are not a student")


# Typecasting = the process of converting a variable from one data type
#      to another str(), float(), bool()
name = "Hendry"
age = 25
gpa = 3.5
is_student = True

gpa =int(gpa)
age =float(age)
age = str(age)

print(age)

# can use typecasting to covert string to boolean determine if character was inputted
# can re prompt the use to input string again
name = bool(name)

print(name)

# User input = A function that prompts the user to enter data
#              Returns the entered data as a string
name = input("What is your name?: ")
print(f"Hello {name}!")

age = input("How old are you?: ")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc
length = float(input("Enter the  length?: "))
width = float(input("Enter the  width?: "))
area = length * width
print(f"The area is {area} cm")

# Exercise 2 shopping cart program
item = int(input("Enter the item: "))
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))
total =price * quantity
print(f"The price is {total}")

# Mad libs game
# Word game where you crete a story
# by filling in blanks with random words

adjective1 =input("Enter the adjective: ")
noun1 = input("Enter the noun: ")
adjective2 =input("Enter the adjective: ")
verb1 = input("Enter the verb ending with 'ing': ")
adjective3 = input("Enter the adjective: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

# Arithmetic expressions

friends= 10
# argument
friends = friends + 1
friends += 1

friends = friends - 1
friends -= 2
friends *= 3
friends = friends / 2
friends =friends ** 2
remainder =friends % 3
print(remainder)

import math

x = 9

print(math.pi)
print(math.e)
results = math.sqrt(x)
# results = math.ceil(x)
# results = math.floor(x)
print(results)

# Circumference
radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"circumference is {round(circumference)}")


# Area of a circle

radius = float(input("Enter the radius of the circle: "))
area =math.pi * radius**2
print(f"area is {round(area,2)}")

# Hypotenuse of right angle triangle
a= float(input("Enter Side A: "))
b= float(input("Enter Side B: "))
c= math.sqrt(pow(a,2)+pow(b,2))

print(f"Side C= {c}")

# If statements = do some code only if some condition is True
#               Else do something else

age = int(input("Enter your age: "))

if age >=18 and 65 <= age:
    print("You are now signed up!")
elif age < 0 :
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to signed up!")
else :
    print("You are not now signed up!")

# Exercise 2
response =input("Would you like food? (Y/N): ")

# when we want to check if the response is true we use dabble ==
if response == "Y" or response == "y":
    print("Have some food!")
else:
    print("Thank you!")

name = input("Enter your name: ")

if name == " ":
    print("You did not enter your name!")
else:
    print(f"Hello {name}")

# boolean
for_sale = True

if for_sale:
    print("The item is for sale")
else:
    print("The item is not for sale")

# python calculator exercise

operator = input("Enter your operator (+ - * /: ")
num1 =int(input("Enter your first number: "))
num2 =int(input("Enter your second number: "))
print(num1+num2)
if operator == "+":
    result = num1+num2
    print(round(result,3))
elif operator == "-":
    result = num1-num2
    print(round(result,3))
elif operator == "*":
    result = num1*num2
    print(round(result,3))
elif operator == "/":
    result = num1/num2
    print(round(result,3))
    print(result)
else:
    print(f"{operator} is  Invalid")

# python weight converter

weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds? (K or L):  ")
if unit == "K":
    weight = weight * 2.205
    unit= "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit= "Kgs."
else:
    print(f"{unit} was not valid")
print(f"Your weight is {round(weight,2)} {unit}")

# temperature converter
unit =input("Is this temperature in Celsius or Fahrenheit? (C or F): ")
temp = float(input("Enter your temperature: "))
if unit == "C":
    temp = round(temp*9/5+32,1)
    print(f"The temperature in Celsius is: {temp} degrees Fahrenheit")
elif unit == "F":
    temp = temp*5/9+273
    print(f"The temperature in Fahrenheit: {temp} degrees Celsius")
else:
    print(f"{unit} was not valid")


# logical operators = evaluate multiple conditions (or, and, not)
#                    or= at least one condition must be True
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)

temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is now raining")


temp2 =25
is_sunny = False

if temp2 > 25 and  is_sunny:
    print("It is HOT outside ")
    print(" It is SUNNY ")

# while loop = execute some code WHILE some condition remains true
name = input("Enter your name: ")
if name == " ":
    print("You did not enter your name!")
else:
    print(f"Hello {name}")
# age
age = int(input("Enter your age"))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

food = input("Enter your favorite food(q to quit): ")
while food != "q":
    print(f"You are like {food}")
    food = input("Enter another favorite food(q to quit): ")
print("Thank you!")

#logical operators
num = int(input("Enter your number between 1 and 100: "))
while num < 1 or num > 100:
    print("Number must be between 1 and 100")
    num = int(input("Enter your number between 1 and 100: "))
print(f"Your number is {num}")

# python compound interest calculator

principle=0
rate = 0
time =0

while True:
    principle = float(input("Enter your principle amount: "))
    if principle <= 0:
        print("principle can't be less than zero")
    else:
        break
while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter time in years: "))
    if time <= 0:
        print("rate can't be less than or equal to zero")
    else:
        break

total = principle * pow((1+rate/100),time)
print(f"Your total Balance is ${round(total,2)}")

# for loops = execute a block of code a fixed number of times
#      You can iterate over a range , string, sequence, etc.
for x in reversed(range(1,11)):
    print(x)
print("HAPPY WEEKEND")

for x in range(1,21):
    if x ==13:
        continue
    else:print(x)
# count down timer

import time


time.sleep(2)

print("HAPPY WEEKEND")

# nested loop = A loop within another loop (outer, inner)
# outer loop:
# inner loop
for x in range(3):
    for y in range(1, 21):
        print(y, end="")
    print()