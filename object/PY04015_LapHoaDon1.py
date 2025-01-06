class HoaDon:
    def __init__(self, ten, cu, moi, id):
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.id = "KH{:02d}".format(id)
        self.tinh()

    def tinh(self):
        self.tong = self.moi - self.cu
        self.gia = 0
        if self.tong <= 50:
            self.gia = self.tong * 102
        elif self.tong <= 100:
            self.gia = 50 * 100 + (self.tong - 50) * 150
            self.gia = self.gia * 1.03
        else:
            self.gia = 50 * 100 + 50 * 150 + (self.tong - 100) * 200
            self.gia = self.gia * 1.05
        self.gia = round(self.gia)

    def __str__(self):
        return self.id + " " + self.ten + " " + str(int(self.gia))


a = []
for i in range(int(input())):
    a.append(HoaDon(input(), int(input()), int(input()), i + 1))
a.sort(key=lambda x: -x.gia)
print(*a, sep="\n")
