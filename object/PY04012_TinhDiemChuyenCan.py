class SV:
    def __init__(self, id, ten, lop):
        self.id = id
        self.ten = ten
        self.lop = lop
    def getScore(self, s):
        res = 10 - s.count("v")*2 - s.count("m")
        self.tt = "0 KDDK" if res <= 0 else res
    def __str__(self):
        return f"{self.id} {self.ten} {self.lop} {self.tt}"
n, list = int(input()), []
for _ in range(n):
    list.append(SV(input(), input(), input()))
for _ in range(n):
    id, s = [x for x in input().split()]
    for i in list:
        if i.id == id:
            i.getScore(s)
            break
print(*list, sep="\n")
        