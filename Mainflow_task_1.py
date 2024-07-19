#Study of basic Python syntax#

print("welcome to the task 1 of this internship")

#basic scripts to performarithmetic operations manipulate strings and use conditional statements

#Arithmetic operations

# Addition
#define two numbers
a = 5
b = 3
addition = a + b
print("Addition:\n", addition)

# Subtraction
subtraction = a - b
print("Subtraction:\n", subtraction)

# Multiplication
multiplication = a * b
print("Multiplication:\n", multiplication)

# Division
division = a / b
print("Division:\n", division) 

# Floor Division (gives the quotient without the remainder)
floor_division = a // b
print("Floor Division:\n", floor_division) 

# Modulus (gives the remainder)
modulus = a % b
print("Modulus:\n", modulus) 

# Exponentiation (a raised to the power of b)
exponentiation = a ** b
print("Exponentiation:\n", exponentiation) 

# String Manipulation in Python

# Define a string
string1 = "Hello"
string2 = "World"

# String Concatenation
concatenated_string = string1 + " " + string2
print(f"Concatenated string: {concatenated_string}")

# Find the length of the string
length_of_string = len(concatenated_string)
print(f"Length of the concatenated string: {length_of_string}")

# Convert to upper case
upper_case_string = concatenated_string.upper()
print(f"String in upper case: {upper_case_string}")

# Convert to lower case
lower_case_string = concatenated_string.lower()
print(f"String in lower case: {lower_case_string}")

# String slicing
# Extract "Hello" from the concatenated string
sliced_string = concatenated_string[:5]
print(f"Sliced string (first 5 characters): {sliced_string}")

# Conditional Statements in Python

# Define a variable
number = 7

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number is zero.")

# Check if the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


#common data structures like lists, dictionaries, and tuples.

# List in Python

# Define a list
fruits = ["apple", "banana", "cherry"]

# Print the entire list
print(f"List of fruits: {fruits}")

# Accessing elements by index
print(f"The first fruit is: {fruits[0]}")  # Indexing starts from 0
print(f"The second fruit is: {fruits[1]}")

# Adding an element to the list
fruits.append("date")
print(f"List after adding a new fruit: {fruits}")

# Removing an element from the list
fruits.remove("banana")
print(f"List after removing a fruit: {fruits}")

# Length of the list
length_of_list = len(fruits)
print(f"Length of the list: {length_of_list}")

# Dictionary in Python

# Define a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Print the entire dictionary
print(f"Person dictionary: {person}")

# Accessing values by key
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding a new key-value pair
person["email"] = "john@example.com"
print(f"Dictionary after adding an email: {person}")

# Removing a key-value pair
del person["age"]
print(f"Dictionary after removing the age: {person}")

# Length of the dictionary
length_of_dict = len(person)
print(f"Length of the dictionary: {length_of_dict}")


# Tuple in Python

# Define a tuple
colors = ("red", "green", "blue")

# Print the entire tuple
print(f"Tuple of colors: {colors}")

# Accessing elements by index
print(f"The first color is: {colors[0]}")
print(f"The second color is: {colors[1]}")

# Length of the tuple
length_of_tuple = len(colors)
print(f"Length of the tuple: {length_of_tuple}")

# Tuples are immutable, so you can't add or remove elements
# But you can concatenate tuples
new_colors = colors + ("yellow",)
print(f"New tuple after concatenation: {new_colors}")

