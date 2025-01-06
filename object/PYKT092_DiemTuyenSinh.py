class Ts:
    def __init__(self, id, ten, diem, dantoc, khuvuc):
        self.id = 'TS{:02d}'.format(id)
        self.ten = self.getTen(ten)
        self.diem = diem + self.getKv(khuvuc) + self.getDt(dantoc)
        self.tt = "Do" if self.diem >= 20.5 else "Truot"
    def getTen(self, ten):
        return ' '.join(i.capitalize() for i in ten.split())
    def getKv(self, kv):
        if kv == "1": return 1.5
        if kv == "2": return 1
        return 0
    def getDt(self, dt):
        return 0 if dt == "Kinh" else 1.5
    def __str__(self):
        return "{} {} {:.1f} {}".format(self.id, self.ten, self.diem, self.tt)
list = []
for i in range(int(input())):
    list.append(Ts(i+1, input(), float(input()), input(), input()))
print(*sorted(list, key=lambda x: (-x.diem, x.id)), sep='\n')