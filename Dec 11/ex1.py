try:
    no1 = 10
    no2 = 1
    print(no1/no2)
#     with open('student.txt','r') as x:
#         x.read()
#         print(x)

except ArithmeticError as e:
    print(e)

except FileNotFoundError as e:
    print(e)

except:
    print('some error found in code')
