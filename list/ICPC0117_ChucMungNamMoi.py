n = int(input())
m = {"-1"}
for i in range(n) :
    x = input()
    m.add(x)
print(len(m) - 1)
# print(len({input() for i in range(int(input()))}))