from datetime import datetime
class Mon:
    def __init__(self, ma, ten):
        self.ten = ten
        self.ma = ma
    def __str__(self):
        return self.ma+ " " + self.ten
class LichThi:
    def __init__(self, ma, ten, ngay, gio, nhom):
        self.ma = 'T{:03d}'.format(ma)
        self.ten = ten
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom 
    def __str__(self):
        return self.ma + " " + str(self.ten) + " " + self.ngay + " " + self.gio + " " + self.nhom
n, m = [int(i) for i in input().split()]
subjects = [Mon(input(), input()) for i in range(n)]
lichthi = []
for i in range(m):
    s = input().split()
    k = s[0]
    for j in subjects:
        if j.ma == k:
           lichthi.append(LichThi(i+1, j, s[1], s[2], s[3]))
           break
lichthi.sort(key = lambda x: (datetime.strptime(x.ngay, '%d/%m/%Y'), datetime.strptime(x.gio, '%H:%M'), x.ma))
print(*lichthi, sep = '\n')    