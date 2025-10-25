x = ["add", 1, 4,5 ,"end",True ,1]
y = ["exit", 1, 4,6 ,"stop",True ,1]
z = set (x)
z2 = set(y)

result = z.difference(z2)
print ("different elements in (x and y) is:",result)
    
