n=int(input())
def prim(x):
    if x<2:
        return False
    if x==2:
        return True
    for i in range(2, x):
        if x%i==0:
            return False

    return True

talalt=False

for p1 in range(2, n):
    for p2 in range(2, n):
        if prim(p1) and prim(p2):
            if p1+p2==n:
                print(p1, p2)
                talalt = True

if not talalt:
    print("No solution")