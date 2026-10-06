n=int(input("Give a number"))
talalt = False
osszeg=0

for x in range(n-1,1,-1):
    osszeg=0

    for i in range(1,x):
        if x%i==0:
            osszeg=osszeg+i

    if osszeg==x and talalt==False:
        print(x)
        talalt=True

if not talalt:
    print("no solution")
