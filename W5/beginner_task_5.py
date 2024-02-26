# Question 1a:

mylist = list(("apple", "Pineapple", 25, 12.6, "cookies"))
print(type(mylist))
print(mylist)

myset = set(("God", "compartability", "goals", "growth", 10))
print(type(myset))
print(myset)

mytuple = tuple(("gold", 1, 0.225, "purple", "ivory", 40))
print(type(mytuple))
print(mytuple)

mydict = dict(name = "Starr", age = 16, country = "United Kingdom", height = 6.4, relationship_status = "complicated")
print(type(mydict))
print(mydict)

# Question 1b:

project_name = ("Python Mentorship Program")
print(project_name[:: -1])
print(project_name.upper())
print(project_name.replace("Python", "Data_Epic"))

# Question 1c:

initial_list = [1, 2, 3, 4, 5]
initial_list.append(6)
print(initial_list)

initial_list = [1, 2, 3, 4, 5]
initial_list.remove(1)
print(initial_list)

initial_list = [1, 2, 3, 4, 5]
another_list = [7, 8, 9]
initial_list.extend(another_list)
print(initial_list)

# Question 1d:

thistuple = (10, 20, 30)
(pens, books, pencils ) = thistuple
print (pens)
print(books)
print(pencils)

# Question 1e:

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set4 = set1.intersection(set2)
print(set4)
set1.intersection_update(set2)
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set5 = set1.symmetric_difference(set2)
print(set5)
set1.symmetric_difference_update(set2)
print(set1)

# Question 1f:

thisdictionary = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
    }
thisdictionary['occupation'] = 'Engineer'
print(thisdictionary)

thisdictionary = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
    }
thisdictionary.update({'age' : 26})
print(thisdictionary)

thisdictionary = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
    }
thisdictionary.pop('city')
print(thisdictionary)

# Question 1g:

