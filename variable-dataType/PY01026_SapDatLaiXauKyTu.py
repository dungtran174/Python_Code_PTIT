t = int(input())
for _ in range(t):
    a = sorted(input())
    b = sorted(input())
    print("Test " + str(_ + 1) + ": " + ("YES" if a == b else "NO"))