x = ["add", 1, 4,5 ,"end",True ,1]
y = ["exit", 1, 4,6 ,"stop",False ,1]
z = ["apple", 1, 2,6 ,"kill",bool ,0]
b1 = set(x)
b2 = set(y)
b3 = set(z)
print(b1)
print(b2)
print(b3)
result = b1.intersection(b2,b3)
print ("common elements of (x , y & z) is:",result)
