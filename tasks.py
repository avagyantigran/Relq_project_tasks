# ================================
# Task 1: Ask the user for their name and print a greeting message
name = input("Enter your name: ")
print("Hello,", name)

# ================================
# Task 2: Take two numbers as input and print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# ================================
# Task 3: Check whether a given number is even or odd
number = int(input("Enter a number to check even or odd: "))
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# ================================
# Task 4: Print numbers from 1 to 10 using a loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# ================================
# Task 5: Find the largest number in a list
numbers = [10, 45, 3, 99, 23]
largest = max(numbers)
print("Largest number in the list:", largest)

# ================================
# Task 6: Function that returns the square of a number
def square(n):
    return n * n

print("Square of 5:", square(5))

# ================================
# Task 7: Count how many vowels are in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# ================================
# Task 8: Print all elements of a list using a for loop
items = ["apple", "banana", "cherry"]
print("List elements:")
for item in items:
    print(item)

# ================================
# Task 9: Print multiplication table up to 10
table_num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(table_num, "x", i, "=", table_num * i)

# ================================
# Task 10: Check if a word is a palindrome
word = input("Enter a word to check palindrome: ")
if word == word[::-1]:
    print("The word is a Palindrome")
else:
    print("The word is NOT a Palindrome")
