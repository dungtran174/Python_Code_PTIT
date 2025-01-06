class Hd3:
    def __init__(self, id, ten, sl, dg, ck):
        self.id = id
        self.ten = ten
        self.sl = sl
        self.dg = dg
        self.ck = ck
        self.tt = dg*sl - ck
    def __str__(self):
        return f"{self.id} {self.ten} {self.sl} {self.dg} {self.ck} {self.tt}"
list = []
for i in range(int(input())):
    list.append(Hd3(input(), input(), int(input()), int(input()), int(input())))
print(*sorted(list, key=lambda x: -x.tt), sep="\n")