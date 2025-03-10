import array as a
ob1 = a.array("i",[4,5,6,3])
ob2 = a.array(ob1.typecode,[i for i in ob1])
print(ob2)