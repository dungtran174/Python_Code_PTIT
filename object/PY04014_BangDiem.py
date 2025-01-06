class HocSinh:
    def __init__(self, id, ten, *list):
        self.id = id
        self.ten = ten
        self.diem = float(
            "{:.1f}".format(
                (sum(float(i) for i in list) + float(list[0]) + float(list[1]))
                / 10
                / 1.2
            )
        )
        if self.diem >= 9:
            self.hl = "XUAT SAC"
        elif self.diem >= 8:
            self.hl = "GIOI"
        elif self.diem >= 7:
            self.hl = "KHA"
        elif self.diem >= 5:
            self.hl = "TB"
        else:
            self.hl = "YEU"

    def __str__(self):
        return self.id + " " + self.ten + " " + str(self.diem) + " " + self.hl


list = [
    HocSinh("HS{0:0>2}".format(i + 1), input(), *input().split())
    for i in range(int(input()))
]
list.sort(key=lambda x: (-x.diem, x.id))
print(*list, sep="\n")