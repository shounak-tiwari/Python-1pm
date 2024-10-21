age = float(input("Enter the age : "))

height = float(input("Enter the height : "))

education = int(input("education\n 10th : 1\n12th : 2\nUG : 3\nPG : 4\n "))


result = ((age >=18) and (age<=22) and (height>=5.7) and ((education ==1) or (education ==2) or (education ==3) or (education ==4)))

print(result) 
