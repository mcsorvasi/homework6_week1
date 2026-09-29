x =int(input())

if 1<=x and x<=31:
    print("January", x)
elif 32<=x and x<=59:
    print("February", x-31)
elif 60<=x and x<=90:
    print("March", x-59)
elif 91<=x and x<=120:
    print("April", x-90)
elif 121<=x and x<=151:
    print("May", x-120)
elif 152<=x and x<=181:
    print("June", x-151)
elif 182<=x and x<=212:
    print("July", x-181)
elif 213<=x and x<=243:
    print("August", x-212)
elif 244<=x and x<=273:
    print("September", x-243)
elif 274<=x and x<=304:
    print("October", x-273)
elif 305<=x and x<=334:
    print("November", x-304)
elif 335<=x and x<=365:
    print("December", x-334)