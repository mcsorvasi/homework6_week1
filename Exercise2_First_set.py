n=int(input())
def prim(x):
    if x<2:
        return False

    for i in range(2, x):
        if x%i==0:
            return False

    return True

talalt=False

for p1 in range(2, n):
    p2=n-p1

if prim(p1) and prim(p2) and talalt==False:
     print(p1, p2)
     talalt=True


if not talalt:
    print("No solution")