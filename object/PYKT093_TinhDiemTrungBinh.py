from math import ceil
class Hs:
    def __init__(self, id, ten, d1, d2, d3):
        self.id = 'SV{:02d}'.format(id)
        self.ten = self.chuanhoa(ten)
        self.tb = (d1*3 + d2*3 + d3*2)/8
    def chuanhoa(self, ten):
        return ' '.join(i.title() for i in ten.strip().split())
    def __str__(self):
        return '{} {} {:.2f} {}'.format(self.id, self.ten, ceil(self.tb*100)/100, self.xl)
list = []
for i in range(int(input())):
    list.append(Hs(i+1, input(), float(input()), float(input()), float(input())))
list.sort(key = lambda x : (-x.tb, x.id))
list[0].xl = 1
for i in range(1, len(list)):
    list[i].xl = list[i-1].xl if list[i].tb == list[i-1].tb else i + 1
print(*list, sep = '\n')
                