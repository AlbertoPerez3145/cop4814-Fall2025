"""
Basic Python Syntax
----------------------------
This file is a guided template for learning Python basics.
Students should fork and clone this repository from Greg's repo.
Explanations and examples will be added by Greg.
"""

# ==========================================================
# 1. PRINTING AND COMMENTS
# ----------------------------------------------------------
# - Print statements
# - Single-line comments
# - Multi-line comments (docstrings)
# ==========================================================

print("Alberto", 1234, 10) # this is how we print in python, everytime you hit commit, you keep a milestone
# Push means that you bring those copies to your project in github, b4 you push you have the modifications locally
# Pull means that someone is making a pull request, someone will read the modifications and say it is good or bad, they'll write comments

"""This 
is
a block
comment
"""

# ==========================================================
# 2. VARIABLES AND DATA TYPES
# ----------------------------------------------------------
# - Strings
# - Integers, floats
# - Booleans
# - Type checking with type()
# ==========================================================

message = "Welcome to FIU"
print(type(message)) # type () is a function too

a = 10
b = 2
print(type(a), type(b))

isOpen = True
print(type(isOpen))

print(message[0])
print(message[7])

# ==========================================================
# 3. BASIC OPERATORS
# ----------------------------------------------------------
# - Arithmetic (+, -, *, /, //, %, **)
# - Comparison (==, !=, >, <, >=, <=)
# - Logical (and, or, not)
# ==========================================================

print(a + b) # addition
print (a - b) # subtraction
print (a * b) # multiplication
print (a / b) # division
print (7 / 2) # division again
print (7 // 2) # integer division
print (a ** b) # exponentiation
print (7 % 2) # Modulus (remainder of the division)

# ==========================================================
# 4. STRING OPERATIONS
# ----------------------------------------------------------
# - Concatenation
# - f-strings
# - Common methods (.upper(), .lower(), .strip(), etc.)
# ==========================================================

first_name = "alberto"
last_name = "perez"

print(first_name + last_name) #Concatenation
print(first_name + " " + last_name)
print(first_name, last_name)

print(f"My name is {first_name.upper()} {last_name.title()}.") #.upper() turns all into capital, .title() capitalizes first letter
print ("2" + "3")
print("***Welcome to Software Dev***".strip('*')) #.strip() removes any part of the string

# ==========================================================
# 5. LISTS
# ----------------------------------------------------------
# - Creating lists
# - Indexing and slicing
# - Adding/removing elements
# - Useful methods (.append(), .remove(), .sort(), etc.)
# ==========================================================

professors = ["greg", "richard", "kianoosh", "debra", "jason", "leo", "heather"]
print(type(professors))
print(professors[0])
print(professors[-1])
print(professors[2:5]) # a:b a is included but b is not, accessing 2, 3, and 4
print(professors[:5]) # starts from the beginning and ends before 5
print(professors[3:]) # accessing indices from 3 to the end
print(professors[:]) # Does everything

professors.append("todd") #.append adds to the end of the list one by one
print(professors)
professors.extend(["michael", "mustafa", "naomi"]) #.extend adds more than one thing, must be as a list though
print(professors)
professors.insert(2, "vyoma") # .insert gives you a place to insert a string
print(professors)
professors.remove("greg")
print(professors)
x = professors.pop(2) # removes whoever is position 2
print(professors, x)
professors.reverse() # reverses order
print(professors)

professors.sort() # sorts in alphabetical order
print(professors)
professors.sort(reverse = True) # reverses the order
print(professors)
# ==========================================================
# 6. TUPLES AND SETS
# ----------------------------------------------------------
# - Tuples: immutable sequences
# - Sets: unique collections
# ==========================================================

grades = (88.3, 78.6, 99.5) # tuples are immutable
print(type(grades))

members = {"greg", "richard", "greg" } # Does not include duplicates, order does not matter
print (members) # this is a going to be the answer of a future assignment :)

# ==========================================================
# 7. DICTIONARIES
# ----------------------------------------------------------
# - Key-value pairs
# - Accessing and modifying values
# - Common methods (.keys(), .values(), .items())
# ==========================================================



# ==========================================================
# 8. CONDITIONALS
# ----------------------------------------------------------
# - if, elif, else
# - Nested conditionals
# ==========================================================



# ==========================================================
# 9. LOOPS
# ----------------------------------------------------------
# - for loops
# - while loops
# - break and continue
# ==========================================================



# ==========================================================
# 10. FUNCTIONS
# ----------------------------------------------------------
# - Defining functions
# - Parameters and return values
# - Default arguments
# ==========================================================



# ==========================================================
# 11. IMPORTING MODULES
# ----------------------------------------------------------
# - Importing built-in modules (e.g., math, random)
# - Using functions from modules
# ==========================================================



# ==========================================================
# 12. ERROR HANDLING (OPTIONAL)
# ----------------------------------------------------------
# - try, except
# - Handling different exception types
# ==========================================================



