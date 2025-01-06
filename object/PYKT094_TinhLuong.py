class Phong:
    def __init__(self, id, ten):
        self.id = id
        self.ten = ten
class Nv:
    def __init__(self, id, ten, lcb, scong, phong):
        self.id = id
        self.ten = ten
        self.lcb = lcb
        self.scong = scong
        self.phong = phong
    def hsluong(self):
        group, years = self.id[0], int(self.id[1:3])
        if group == 'A':
            if years >= 1 and years <= 3:   return 10
            if years >= 4 and years <= 8:   return 12
            if years >= 9 and years <= 15:   return 14
            if years >= 16:   return 20
        elif group == 'B':
            if years >= 1 and years <= 3:   return 10
            if years >= 4 and years <= 8:   return 11
            if years >= 9 and years <= 15:   return 13
            if years >= 16:   return 16
        elif group == 'C':
            if years >= 1 and years <= 3:   return 9
            if years >= 4 and years <= 8:   return 10
            if years >= 9 and years <= 15:   return 12
            if years >= 16:   return 14
        elif group == 'D':
            if years >= 1 and years <= 3:   return 8
            if years >= 4 and years <= 8:   return 9
            if years >= 9 and years <= 15:   return 11
            if years >= 16:   return 13
        return 0
    def luong(self):
        return self.lcb * self.hsluong() * self.scong
    def __str__(self):
        return f'{self.id} {self.ten} {self.phong.ten} {self.luong()*1000}'
phong = []
nv = []
for i in range(int(input())):
    s = input()
    phong.append(Phong(s[:2], s[3:]))
for i in range(int(input())):
    id = input()
    deId = id[-2:]
    for p in phong:
        if p.id == deId:
            nv.append(Nv(id, input(), int(input()), int(input()), p))
            break
print(*nv, sep='\n')