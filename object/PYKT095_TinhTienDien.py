class Khach:
    def __init__(self, id, ten, type, bd, kt):
        self.id = "KH{:02d}".format(id)
        self.ten = self.chuan_hoa(ten)
        self.chuan = self.getChuan(type)
        self.tong = kt - bd

    def chuan_hoa(self, ten):
        return " ".join(i.capitalize() for i in ten.strip().split())

    def getChuan(self, type):
        if type == "A":
            return 100
        if type == "B":
            return 500
        return 200

    def duoichuan(self):
        return min(self.tong, self.chuan) * 450

    def vuotchuan(self):
        diff = self.tong - self.chuan
        return 0 if diff <= 0 else diff * 1000

    def getVAT(self):
        return self.vuotchuan() // 20

    def getTong(self):
        return self.vuotchuan() + self.getVAT() + self.duoichuan()

    def __str__(self):
        return "{} {} {} {} {} {}".format(
            self.id,
            self.ten,
            self.duoichuan(),
            self.vuotchuan(),
            self.getVAT(),
            self.getTong(),
        )


list = []
for i in range(int(input())):
    name, s = input(), input().split()
    list.append(Khach(i + 1, name, s[0], int(s[1]), int(s[2])))
print(*sorted(list, key=lambda e: -e.getTong()), sep="\n")
