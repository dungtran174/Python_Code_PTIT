from datetime import datetime
class VDV:
    def __init__(self, ten, dd, tg):
        a = [i[0] for i in ten.split()]
        b = [i[0] for i in dd.split()]
        self.id = ''.join(b) + ''.join(a)
        self.ten = ten
        self.dd = dd
        time = datetime.strptime(tg, '%H:%M') - datetime.strptime('6:00', '%H:%M')
        self.td = 120/time.seconds*3600
    def __str__(self):
        return f'{self.id} {self.ten} {self.dd} {round(self.td)} Km/h'
list = []
for i in range(int(input())):
    a = VDV(input(), input(), input())
    list.append(a)
print(*sorted(list, key = lambda x : -x.td), sep = '\n')