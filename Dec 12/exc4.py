try:
    t1 = (1,2,3,4,5)
    t1[2] ='a'
    print(t1)

except TypeError as e:
    print(e)