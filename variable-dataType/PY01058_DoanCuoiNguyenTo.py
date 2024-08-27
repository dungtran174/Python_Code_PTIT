from math import sqrt
def nto(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    t = int(input())
    for i in range(t) :
        s = input()
        if nto(int(s[-4::])): 
            print("YES")
        else: 
            print("NO")  