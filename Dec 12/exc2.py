# num1 = 8.459746251804146e+25
# num2 = 1e-308

# print(num1*num2)

no1 = 10
no2 = 0

try:
    print(no1/no2)

except FloatingPointError as e:
    print(e)