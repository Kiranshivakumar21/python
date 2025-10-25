a = ["add", 1, 4,5 ,"end",True ,1]
b = ["exit", 1, 4,6 ,"stop",False ,1]
z1 = set(a)
z2 = set(b)
print(z1)
print(z2)
result = z1.intersection(z2)
print ("common elements of (a & b) is:",result)
