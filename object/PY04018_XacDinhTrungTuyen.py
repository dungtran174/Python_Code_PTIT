class GV:
    def __init__(self, i, ten, code, diem1, diem2):
        self.i = "GV{:02d}".format(i)
        self.ten = ten
        self.code = code
        self.tong = diem1 * 2 + diem2 + self.getUuTien(code)
        self.sj = self.getSj(code)

    def getSj(self, code):
        if code[0] == "A":
            return "TOAN"
        if code[0] == "B":
            return "LY"
        return "HOA"

    def getUuTien(self, code):
        if code[1] == "1":
            return 2
        if code[1] == "2":
            return 1.5
        if code[1] == "3":
            return 1
        return 0

    def getTT(self):
        if self.tong >= 18:
            return "TRUNG TUYEN"
        return "LOAI"

    def __str__(self):
        return "{} {} {} {:.1f} {}".format(
            self.i, self.ten, self.sj, self.tong, self.getTT()
        )


list = []
for i in range(int(input())):
    list.append(GV(i + 1, input(), input(), float(input()), float(input())))
list.sort(key=lambda x: -x.tong)
print(*list, sep="\n")
