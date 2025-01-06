from datetime import datetime
class nhanghi:
    def __init__(self, i, ten, phong, den, di, phi):
        self.i = 'KH{:02d}'.format(i) 
        self.ten = ten
        self.phong = phong
        time = datetime.strptime(di, '%d/%m/%Y') - datetime.strptime(den, '%d/%m/%Y')
        self.days = time.days + 1
        self.phi = phi
    def getTong(self):
        if self.phong[0] == '1': 
            return self.days * 25  + self.phi
        elif self.phong[0] == '2':
            return self.days * 34 + self.phi
        elif self.phong[0] == '3':
            return self.days * 50 + self.phi
        else:
            return self.days * 80 + self.phi
    def __str__(self): 
        return f'{self.i} {self.ten} {self.phong} {self.days} {self.getTong()}'
list1 = []
n = int(input())
for i in range(1, n+1):
    list1.append(nhanghi(i, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
list1.sort(key=lambda x: x.getTong(), reverse=True)
print(*list1, sep='\n')