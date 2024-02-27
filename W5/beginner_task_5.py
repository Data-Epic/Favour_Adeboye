# Question 1a:

mylist = list(("apple", "Pineapple", 25, 12.6, "cookies"))      # Creating a list
print(type(mylist))                                             # Printing the type of mylist
print(mylist)                                                   # Printing the contents of mylist

myset = set(("God", "compartability", "goals", "growth", 10))   # Creating a set
print(type(myset))                                              # Printing the type of myset
print(myset)                                                    # Printing the contents of myset

mytuple = tuple(("gold", 1, 0.225, "purple", "ivory", 40))      # Creating a tuple
print(type(mytuple))                                            # Printing the type of mytuple
print(mytuple)                                                  # Printing the contents of mytuple

mydict = dict(name = "Starr", age = 16, country = "United Kingdom", height = 6.4, relationship_status = "complicated") # Creating a dictionary
print(type(mydict))                                             # Printing the type of mydic
print(mydict)                                                   # Printing the contents of mydic

# Question 1b:

# Manipulating string variables
project_name = ("Python Mentorship Program")
print(project_name[:: -1])                                      # Reversing the string
print(project_name.upper())                                     # Converting the string to uppercase
print(project_name.replace("Python", "Data_Epic"))              # Replacing substring

# Question 1c:

# Manipulating lists
initial_list = [1, 2, 3, 4, 5]
initial_list.append(6)                                          # Appending an element
print(initial_list)

initial_list = [1, 2, 3, 4, 5]
initial_list.remove(1)                                          # Removing an element
print(initial_list)

initial_list = [1, 2, 3, 4, 5]
another_list = [7, 8, 9]
initial_list.extend(another_list)                               # Extending the list
print(initial_list)

# Question 1d:

# Unpacking a tuple into variables
thistuple = (10, 20, 30)
(pens, books, pencils ) = thistuple
print (pens)
print(books)
print(pencils)

# Question 1e:

# Performing set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.union(set2)                                         # Joining two sets together to form a new set
print(set3)
set1.update(set2)                                               # Adding the values of set2 to set1
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set4 = set1.intersection(set2)                                  # Putting similar values between two sets to form a new set
print(set4)
set1.intersection_update(set2)                                  # Picking the similarities between two sets
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set5 = set1.symmetric_difference(set2)                          # Putting disimilar values between two sets to form a new set
print(set5)
set1.symmetric_difference_update(set2)                          # Picking the disimilaties between two sets
print(set1)

# Question 1f:

# Manipulating dictionaries
thisdictionary = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
    }
thisdictionary['occupation'] = 'Engineer'                        # Adding a new key-value pair
print(thisdictionary)

thisdictionary = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
    }
thisdictionary.update({'age' : 26})                               # Updating a value
print(thisdictionary)

thisdictionary = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
    }
thisdictionary.pop('city')                                         # Removing a key-value pair
print(thisdictionary)

# Question 1g:

# Converting between data types
thestring = ("123")
a = int(thestring)                                                 # Converting from string to integer
print(a)
thelist = [1, 2, 3]
b = set(thelist)                                                   # Converting from list to set
print(b)

# Question 1h:

# Performing arithmetic operations
x = 5
y = 10
print(x + y)                                                        # Addition operation
print(x - y)                                                        # Substraction operation
print(x * y)                                                        # Multiplication operation
print(x / y)                                                        # Division operation
print(x ** y)                                                       # Eponentioation operation 

# Question 1i:

# Using comparison operators and conditional statements
print(x > y)
print(x == 5)
print(y != 10)

if x > y:
    print("x is greater than y")
elif x == 5:
    print("x equals 5")
elif y != 10:
    print("y is not equal to 10")
else:
    print("None of the conditions are met")

# Question 1j:

# Conditional statement based on a variable value
variablescore = 85
if variablescore >= 60:
    print("Pass")
else:
    print("Fail")
