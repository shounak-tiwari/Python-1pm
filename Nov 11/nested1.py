"""
    if user want to fill codevita tcs career form then user have to follow some conditions 
    1. age >=18 and age <=27
    2. user_10th_percentage >=55%
    3. user_12th_percentage >= 55%
    4. user_have completed their graduation with  55% or above 

        user can eligible otherwise user not able to fill form of codevita tcs career
"""
# 11/07/2004
# current date 
# age 

age = int(input("Enter the age : "))

if 27>= age >=18:
    user_10th = float(input("Enter the 10th class percentage : "))
    if user_10th>=55.00:
        user_12th = float(input("Enter the 12th class percentage : "))
        if user_12th >=55.00:
            graduation = float(input("enter final degree percentage : "))
            if graduation>=55.00:
                print("yes! your eligible for tcs code vita ")
            else:
                print("Your graduation marks is not matched ")
        else:
            print("your 12th marks is not matched ")
    else:
        print('your 10th marks is not matched ')
else:
    print('user age is not matched ')