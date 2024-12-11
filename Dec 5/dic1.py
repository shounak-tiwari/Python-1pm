stud_rec = {}
name = input('Enter the name of student  : ')

stud_rec['key'] = name

print(stud_rec)

marks = dict()

marks['data_science'] = float(input('Enter the marks in data science : '))

marks['artifical_int'] = float(input('Enter the marks in artifical_int : '))

marks['Python'] = float(input('enter the marks in Python : '))

marks['machine_learning'] = float(input('Enter the marks of machine_learning : '))

marks['robotics'] = float(input('Enter the marks of robotics : '))


stud_rec['marks'] = marks

print(stud_rec)