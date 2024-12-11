name  = input('Enter the  name : ')
add = input('Enter the address : ')
pin = input('Enter the  pin : ')
income = input('Enter the income : ') 

# create new file for creating new file using open function 
# open function is use for opening new or existing file if file is already present open function open that file and if file not present in given path file is automatically created by open function but take care of things function have write  or append mode if we dont have write mode we can not able to create new file , read update and delete file want existing file if we dont have it return error file not found...

# create new file with name writemode_demo.txt 

file = open('writemode_demo.txt','w')

file.write(f"Name  : {name}\nAddress : {add}\nPin : {pin}\nIncome : {income}")


file.close()