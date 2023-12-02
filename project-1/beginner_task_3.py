# Display a Welcome message
print ('Hello World!')

# Prompt the user to enter their name and store it in the 'name' variable
name = input ('Enter your name: ')

# Prompt the user to enter their age and store it in the 'age' variable
age = input ('Enter your age: ')

# Prompt the user to indicate whether they are a student or not, and store it in the 'is_student' variable
is_student = input ('Are you a student? (yes/no): ') 

# Convert the 'is_student' response to lowercase and check if it is 'yes', storing the result in 'is_student_bool'
is_student_bool = is_student.lower() == "yes"

# Display a message including the entered name, age, and whether the person is a student or not
print (name, 'is', age, 'years old. Is', name, 'a student?:', is_student_bool)