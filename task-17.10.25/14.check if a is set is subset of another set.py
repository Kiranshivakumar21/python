#if a set is subset of another set

x = {"add", 1, 4,5 ,"stop",True}
y = {"add", 1, 4,5 ,"stop",True ,6 , "scopetech" ,"test"}
z = {"kiran" ,33.3, "vishwa" ,"add", 1, 4,5 ,"stop",True}
subset = x.issubset(y)
anotherset_z = x.issubset(z)
print ("a set is subset of (x and y) is:",subset)
print ("a set is subset of another set (x and z) is:",anotherset_z)
    
    
