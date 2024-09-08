n = input()
h = 0
while len(n) > 1:
    sum = 0
    for i in n:
        sum += ord(i) - 48
    n = str(sum)
    h += 1
print(h)
