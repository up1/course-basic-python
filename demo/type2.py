mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
    print("Float: %.2f" % myfloat)
    print("Float: %.2f %d" % (myfloat, myint))
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
