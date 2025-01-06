from math import factorial as f

for i in range(int(input())):
    n = int(input())
    if n == sum([f(int(x)) for x in str(n)]):
        print("Yes")
    else:
        print("No")
