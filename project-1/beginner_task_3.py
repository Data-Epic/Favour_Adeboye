print ('Hello World!')

name = input ('Enter your name: ')
age = input ('Enter your age: ')
is_student = input ('Are you a student? (yes/no): ')

is_student_bool = is_student.lower() == 'yes'

print (name, 'is', age, 'years old. Is', name, 'a student?:', is_student_bool)