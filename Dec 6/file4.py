import os

current_location = os.getcwd()

print(current_location)


# open_file = os.open('/home/administrator/Desktop','student.txt')
# os.mkdir('/home/administrator/Desktop/new folder/new.txt','w')
import os

folder_location = "/home/administrator/Desktop/classes/python/Python 1pm/Dec 6"
file_name = "student_rec1.txt"

file_path = os.path.join(folder_location, file_name)

os.makedirs(folder_location, exist_ok=True)  

with open(file_path, 'w') as x:
    x.write('file is created')


