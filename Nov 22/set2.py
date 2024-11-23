s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {5,6,7,8,1,2}

print("original set no 1 : ",s1)

print("original set no 2 : ",s2)

diff =  s1.difference(s2)

print(diff)


issuper = s1.issuperset(s2)

print(issuper)

issuper = s2.issuperset(s1)
print(issuper)


