limit = int (input("enter the multiplcation table"))
for i in range (1, limit + 1):
   for j in range (1,11):
      print ("{}*{}={}".format(i ,j, i*j))
   print ()
